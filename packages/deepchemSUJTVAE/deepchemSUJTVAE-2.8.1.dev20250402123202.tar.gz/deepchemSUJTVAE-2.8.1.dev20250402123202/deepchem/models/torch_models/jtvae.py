import copy
import logging
import math
import sys
import numpy as np
import rdkit.Chem as Chem
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch.optim.lr_scheduler as lr_scheduler
from deepchem.utils.jtvae_utils import MolTreeFolder, Vocab, attach_mols,copy_edit_mol,enum_assemble,set_atommap,tensorize,JTMPN,MolTree,MPN,create_var
from deepchem.models.torch_models.jtnn_enc import JTNNEncoder
from deepchem.models.torch_models.jtnn_dec import JTNNDecoder
class JTNNVAE(nn.Module):
    def __init__(self, vocab, hidden_size, latent_size, depthT, depthG):
        super(JTNNVAE, self).__init__()
        self.vocab = vocab
        self.hidden_size = hidden_size
        self.latent_size = latent_size = (
            latent_size // 2
        )  # Tree and Mol has two vectors

        self.jtnn = JTNNEncoder(
            hidden_size, depthT, nn.Embedding(vocab.size(), hidden_size)
        )
        self.decoder = JTNNDecoder(
            vocab, hidden_size, latent_size, nn.Embedding(vocab.size(), hidden_size)
        )

        self.jtmpn = JTMPN(hidden_size, depthG)
        self.mpn = MPN(hidden_size, depthG)

        self.A_assm = nn.Linear(latent_size, hidden_size, bias=False)
        self.assm_loss = nn.CrossEntropyLoss(size_average=False)

        self.T_mean = nn.Linear(hidden_size, latent_size)
        self.T_var = nn.Linear(hidden_size, latent_size)
        self.G_mean = nn.Linear(hidden_size, latent_size)
        self.G_var = nn.Linear(hidden_size, latent_size)

    def encode(self, jtenc_holder, mpn_holder):
        tree_vecs, tree_mess = self.jtnn(*jtenc_holder)
        mol_vecs = self.mpn(*mpn_holder)
        return tree_vecs, tree_mess, mol_vecs

    def encode_from_smiles(self, smiles_list):
        tree_batch = [MolTree(s) for s in smiles_list]
        _, jtenc_holder, mpn_holder = tensorize(tree_batch, self.vocab, assm=False)
        tree_vecs, _, mol_vecs = self.encode(jtenc_holder, mpn_holder)
        return torch.cat([tree_vecs, mol_vecs], dim=-1)

    def encode_latent(self, jtenc_holder, mpn_holder):
        tree_vecs, _ = self.jtnn(*jtenc_holder)
        mol_vecs = self.mpn(*mpn_holder)
        tree_mean = self.T_mean(tree_vecs)
        mol_mean = self.G_mean(mol_vecs)
        tree_var = -torch.abs(self.T_var(tree_vecs))
        mol_var = -torch.abs(self.G_var(mol_vecs))
        return torch.cat([tree_mean, mol_mean], dim=1), torch.cat(
            [tree_var, mol_var], dim=1
        )

    def rsample(self, z_vecs, W_mean, W_var):
        batch_size = z_vecs.size(0)
        z_mean = W_mean(z_vecs)
        z_log_var = -torch.abs(W_var(z_vecs))  # Following Mueller et al.
        kl_loss = (
            -0.5
            * torch.sum(1.0 + z_log_var - z_mean * z_mean - torch.exp(z_log_var))
            / batch_size
        )
        epsilon = create_var(torch.randn_like(z_mean))
        z_vecs = z_mean + torch.exp(z_log_var / 2) * epsilon
        return z_vecs, kl_loss

    def sample_prior(self, prob_decode=False):
        z_tree = torch.randn(1, self.latent_size).cuda()
        z_mol = torch.randn(1, self.latent_size).cuda()
        return self.decode(z_tree, z_mol, prob_decode)

    def forward(self, x_batch, beta):
        x_batch, x_jtenc_holder, x_mpn_holder, x_jtmpn_holder = x_batch
        x_tree_vecs, x_tree_mess, x_mol_vecs = self.encode(x_jtenc_holder, x_mpn_holder)
        z_tree_vecs, tree_kl = self.rsample(x_tree_vecs, self.T_mean, self.T_var)
        z_mol_vecs, mol_kl = self.rsample(x_mol_vecs, self.G_mean, self.G_var)

        kl_div = tree_kl + mol_kl
        word_loss, topo_loss, word_acc, topo_acc = self.decoder(x_batch, z_tree_vecs)
        assm_loss, assm_acc = self.assm(
            x_batch, x_jtmpn_holder, z_mol_vecs, x_tree_mess
        )

        return (
            word_loss + topo_loss + assm_loss + beta * kl_div,
            kl_div.item(),
            word_acc,
            topo_acc,
            assm_acc,
        )

    def assm(self, mol_batch, jtmpn_holder, x_mol_vecs, x_tree_mess):
        jtmpn_holder, batch_idx = jtmpn_holder
        fatoms, fbonds, agraph, bgraph, scope = jtmpn_holder
        batch_idx = create_var(batch_idx)

        cand_vecs = self.jtmpn(fatoms, fbonds, agraph, bgraph, scope, x_tree_mess)

        x_mol_vecs = x_mol_vecs.index_select(0, batch_idx)
        x_mol_vecs = self.A_assm(x_mol_vecs)  # bilinear
        scores = torch.bmm(x_mol_vecs.unsqueeze(1), cand_vecs.unsqueeze(-1)).squeeze()

        cnt, tot, acc = 0, 0, 0
        all_loss = []
        for i, mol_tree in enumerate(mol_batch):
            comp_nodes = [
                node
                for node in mol_tree.nodes
                if len(node.cands) > 1 and not node.is_leaf
            ]
            cnt += len(comp_nodes)
            for node in comp_nodes:
                label = node.cands.index(node.label)
                ncand = len(node.cands)
                cur_score = scores.narrow(0, tot, ncand)
                tot += ncand

                if cur_score.data[label] >= cur_score.max().item():
                    acc += 1

                label = create_var(torch.LongTensor([label]))
                all_loss.append(self.assm_loss(cur_score.view(1, -1), label))

        all_loss = sum(all_loss) / len(mol_batch)
        return all_loss, acc * 1.0 / cnt

    def decode(self, x_tree_vecs, x_mol_vecs, prob_decode):
        # currently do not support batch decoding
        assert x_tree_vecs.size(0) == 1 and x_mol_vecs.size(0) == 1

        pred_root, pred_nodes = self.decoder.decode(x_tree_vecs, prob_decode)
        if len(pred_nodes) == 0:
            return None
        elif len(pred_nodes) == 1:
            return pred_root.smiles

        # Mark nid & is_leaf & atommap
        for i, node in enumerate(pred_nodes):
            node.nid = i + 1
            node.is_leaf = len(node.neighbors) == 1
            if len(node.neighbors) > 1:
                set_atommap(node.mol, node.nid)

        scope = [(0, len(pred_nodes))]
        jtenc_holder, mess_dict = JTNNEncoder.tensorize_nodes(pred_nodes, scope)
        _, tree_mess = self.jtnn(*jtenc_holder)
        tree_mess = (
            tree_mess,
            mess_dict,
        )  # Important: tree_mess is a matrix, mess_dict is a python dict

        x_mol_vecs = self.A_assm(x_mol_vecs).squeeze()  # bilinear

        cur_mol = copy_edit_mol(pred_root.mol)
        global_amap = [{}] + [{} for node in pred_nodes]
        global_amap[1] = {atom.GetIdx(): atom.GetIdx() for atom in cur_mol.GetAtoms()}

        cur_mol, _ = self.dfs_assemble(
            tree_mess,
            x_mol_vecs,
            pred_nodes,
            cur_mol,
            global_amap,
            [],
            pred_root,
            None,
            prob_decode,
            check_aroma=True,
        )
        if cur_mol is None:
            cur_mol = copy_edit_mol(pred_root.mol)
            global_amap = [{}] + [{} for node in pred_nodes]
            global_amap[1] = {
                atom.GetIdx(): atom.GetIdx() for atom in cur_mol.GetAtoms()
            }
            cur_mol, pre_mol = self.dfs_assemble(
                tree_mess,
                x_mol_vecs,
                pred_nodes,
                cur_mol,
                global_amap,
                [],
                pred_root,
                None,
                prob_decode,
                check_aroma=False,
            )
            if cur_mol is None:
                cur_mol = pre_mol

        if cur_mol is None:
            return None

        cur_mol = cur_mol.GetMol()
        set_atommap(cur_mol)
        cur_mol = Chem.MolFromSmiles(Chem.MolToSmiles(cur_mol))
        return Chem.MolToSmiles(cur_mol) if cur_mol is not None else None

    def main_vae_train(
    train,
    vocab,
    save_dir,
    load_epoch=0,
    hidden_size=450,
    batch_size=32,
    latent_size=56,
    depthT=20,
    depthG=3,
    lr=1e-3,
    clip_norm=50.0,
    beta=0.0,
    step_beta=0.002,
    max_beta=1.0,
    warmup=40000,
    epoch=20,
    anneal_rate=0.9,
    anneal_iter=40000,
    kl_anneal_iter=2000,
    print_iter=50,
    save_iter=5000,
    num_workers=4,
):
        
        vocab = [x.strip("\r\n ") for x in open(vocab)]
        vocab = Vocab(vocab)

        model = JTNNVAE(vocab, hidden_size, latent_size, depthT, depthG)
        print(model)

        for param in model.parameters():
            if param.dim() == 1:
                nn.init.constant_(param, 0)
            else:
                nn.init.xavier_normal_(param)

        if load_epoch > 0:
            model.load_state_dict(torch.load(save_dir + "/model.iter-" + str(load_epoch)))

        print(
            "Model #Params: %dK" % (sum([x.nelement() for x in model.parameters()]) / 1000,)
        )

        optimizer = optim.Adam(model.parameters(), lr=lr)
        scheduler = lr_scheduler.ExponentialLR(optimizer, anneal_rate)
        scheduler.step()

        param_norm = lambda m: math.sqrt(
            sum([p.norm().item() ** 2 for p in m.parameters()])
        )
        grad_norm = lambda m: math.sqrt(
            sum([p.grad.norm().item() ** 2 for p in m.parameters() if p.grad is not None])
        )

        total_step = load_epoch
        beta = beta
        meters = np.zeros(4)

        for epoch in range(epoch):
            loader = MolTreeFolder(train, vocab, batch_size, num_workers=num_workers)
            for batch in loader:
                total_step += 1
                try:
                    model.zero_grad()
                    loss, kl_div, wacc, tacc, sacc = model(batch, beta)
                    loss.backward()
                    nn.utils.clip_grad_norm_(model.parameters(), clip_norm)
                    optimizer.step()
                except Exception as e:
                    logging.exception(e)
                # raise e
                # print(e)
                # continue

                meters = meters + np.array([kl_div, wacc * 100, tacc * 100, sacc * 100])

                if total_step % print_iter == 0:
                    meters /= print_iter
                    print(
                        "[%d] Beta: %.3f, KL: %.2f, Word: %.2f, Topo: %.2f, Assm: %.2f, PNorm: %.2f, GNorm: %.2f"
                        % (
                            total_step,
                            beta,
                            meters[0],
                            meters[1],
                            meters[2],
                            meters[3],
                            param_norm(model),
                            grad_norm(model),
                        )
                    )
                    sys.stdout.flush()
                    meters *= 0

                if total_step % save_iter == 0:
                    torch.save(
                        model.state_dict(), save_dir + "/model.iter-" + str(total_step)
                    )

                if total_step % anneal_iter == 0:
                    scheduler.step()
                    print("learning rate: %.6f" % scheduler.get_lr()[0])

                if total_step % kl_anneal_iter == 0 and total_step >= warmup:
                    beta = min(max_beta, beta + step_beta)
        torch.save(model.state_dict(), save_dir + "/model.completed")
        return model


    def dfs_assemble(
        self,
        y_tree_mess,
        x_mol_vecs,
        all_nodes,
        cur_mol,
        global_amap,
        fa_amap,
        cur_node,
        fa_node,
        prob_decode,
        check_aroma,
    ):
        fa_nid = fa_node.nid if fa_node is not None else -1
        prev_nodes = [fa_node] if fa_node is not None else []

        children = [nei for nei in cur_node.neighbors if nei.nid != fa_nid]
        neighbors = [nei for nei in children if nei.mol.GetNumAtoms() > 1]
        neighbors = sorted(neighbors, key=lambda x: x.mol.GetNumAtoms(), reverse=True)
        singletons = [nei for nei in children if nei.mol.GetNumAtoms() == 1]
        neighbors = singletons + neighbors

        cur_amap = [(fa_nid, a2, a1) for nid, a1, a2 in fa_amap if nid == cur_node.nid]
        cands, aroma_score = enum_assemble(cur_node, neighbors, prev_nodes, cur_amap)
        if len(cands) == 0 or (sum(aroma_score) < 0 and check_aroma):
            return None, cur_mol

        cand_smiles, cand_amap = list(zip(*cands))
        aroma_score = torch.Tensor(aroma_score).cuda()
        cands = [(smiles, all_nodes, cur_node) for smiles in cand_smiles]

        if len(cands) > 1:
            jtmpn_holder = JTMPN.tensorize(cands, y_tree_mess[1])
            fatoms, fbonds, agraph, bgraph, scope = jtmpn_holder
            cand_vecs = self.jtmpn(
                fatoms, fbonds, agraph, bgraph, scope, y_tree_mess[0]
            )
            scores = torch.mv(cand_vecs, x_mol_vecs) + aroma_score
        else:
            scores = torch.Tensor([1.0])

        if prob_decode:
            probs = (
                F.softmax(scores.view(1, -1), dim=1).squeeze() + 1e-7
            )  # prevent prob = 0
            cand_idx = torch.multinomial(probs, probs.numel())
        else:
            _, cand_idx = torch.sort(scores, descending=True)

        backup_mol = Chem.RWMol(cur_mol)
        pre_mol = cur_mol
        for i in range(cand_idx.numel()):
            cur_mol = Chem.RWMol(backup_mol)
            pred_amap = cand_amap[cand_idx[i].item()]
            new_global_amap = copy.deepcopy(global_amap)

            for nei_id, ctr_atom, nei_atom in pred_amap:
                if nei_id == fa_nid:
                    continue
                new_global_amap[nei_id][nei_atom] = new_global_amap[cur_node.nid][
                    ctr_atom
                ]

            cur_mol = attach_mols(
                cur_mol, children, [], new_global_amap
            )  # father is already attached
            new_mol = cur_mol.GetMol()
            new_mol = Chem.MolFromSmiles(Chem.MolToSmiles(new_mol))

            if new_mol is None:
                continue

            has_error = False
            for nei_node in children:
                if nei_node.is_leaf:
                    continue
                tmp_mol, tmp_mol2 = self.dfs_assemble(
                    y_tree_mess,
                    x_mol_vecs,
                    all_nodes,
                    cur_mol,
                    new_global_amap,
                    pred_amap,
                    nei_node,
                    cur_node,
                    prob_decode,
                    check_aroma,
                )
                if tmp_mol is None:
                    has_error = True
                    if i == 0:
                        pre_mol = tmp_mol2
                    break
                cur_mol = tmp_mol

            if not has_error:
                return cur_mol, cur_mol

        return None, pre_mol
    


