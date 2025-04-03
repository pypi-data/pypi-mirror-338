import numpy as np
import torch
import torch.nn as nn
import gc


def pairwise_distances(a: np.ndarray, b: np.ndarray, p: int = 2) -> np.ndarray:
    """Compute batched pairwise distance matrices."""
    return np.linalg.norm(a[:, :, np.newaxis] - b[:, np.newaxis], axis=-1, ord=p)

def sinkhorn(a: np.ndarray, 
             b: np.ndarray, 
             M: np.ndarray, 
             eps: float, 
             max_iters: int = 100, 
             stop_thresh: float = 1e-3) -> np.ndarray:
    """Sinkhorn algorithm for optimal transport."""
    u, v = np.zeros_like(a), np.zeros_like(b)
    M_t = np.transpose(M, axes=(0, 2, 1))

    for _ in range(max_iters):
        u_prev, v_prev = u.copy(), v.copy()
        u = eps * (np.log(a) - np.log(np.sum(np.exp((v[:, None] - M)/eps), axis=2)))
        v = eps * (np.log(b) - np.log(np.sum(np.exp((u[:, None] - M_t)/eps), axis=2)))
        
        if np.max(np.abs(u - u_prev)) < stop_thresh and np.max(np.abs(v - v_prev)) < stop_thresh:
            break
    
    return np.exp((u[:, :, None] + v[:, None] - M)/eps)

def earth_movers_distance(p: np.ndarray, 
                          q: np.ndarray, 
                          p_norm: int = 2, 
                          eps: float = 1e-4) -> float:
    """Compute EMD between two point clouds."""
    M = pairwise_distances(p[np.newaxis], q[np.newaxis], p_norm)
    a = np.ones(p.shape[0])/p.shape[0]
    b = np.ones(q.shape[0])/q.shape[0]
    P = sinkhorn(a[np.newaxis], b[np.newaxis], M, eps)
    return (P * M).sum().item()


# ----------------- Earth Mover's Distance -----------------
class EMDLoss(nn.Module):
    def __init__(self, eps=0.005, max_iter=100):
        super().__init__()
        self.eps = eps
        self.max_iter = max_iter
        self.iteration = 0

    def forward(self, p1: torch.Tensor, 
               p2: torch.Tensor, 
               p_norm: int = 2,
               reduce_mean: bool = True, device = torch.device("cuda" if torch.cuda.is_available() else "cpu")) -> torch.Tensor:
        """
        Batched EMD with Sinkhorn Algorithm
        Args:
            p1: (B, N, D) tensor (assumes uniform weights)
            p2: (B, M, D) tensor (assumes uniform weights)
            p_norm: norm type (1 or 2)
            reduce_mean: whether to average over batch
        Returns:
            (B,) tensor of EMD distances or scalar if reduce_mean=True
        """
        B, N, D = p1.shape
        M = p2.shape[1]
        
        # 统一化权重
        a = torch.ones(B, N, device=device) / N  # (B, N)
        b = torch.ones(B, M, device=device) / M  # (B, M)
        
        # 成对距离矩阵
        dist = torch.cdist(p1, p2, p=p_norm)  # (B, N, M)
        
        # Sinkhorn迭代
        u = torch.zeros_like(a)
        v = torch.zeros_like(b)
        
        for _ in range(self.max_iter):
            u_prev = u
            v_prev = v
            
            # 更新u
            v_exp = v.unsqueeze(1) - dist  # (B, 1, M) - (B, N, M) => (B, N, M)
            u = self.eps * (torch.log(a + 1e-8) - torch.logsumexp(v_exp / self.eps, dim=2))
            
            # 更新v
            u_exp = u.unsqueeze(2) - dist  # (B, N, 1) - (B, N, M) => (B, N, M)
            v = self.eps * (torch.log(b + 1e-8) - torch.logsumexp(u_exp / self.eps, dim=1))
            
            # 收敛判断
            if torch.max(torch.abs(u - u_prev)) < 1e-3 and torch.max(torch.abs(v - v_prev)) < 1e-3:
                break
        
        # 计算传输矩阵
        P = torch.exp((u.unsqueeze(2) + v.unsqueeze(1) - dist) / self.eps)
        
        # 计算EMD
        emd = torch.sum(P * dist, dim=(1,2))  # (B,)
        
        res = torch.mean(emd) if reduce_mean else emd
        
        del dist, u, v, u_prev, v_prev, v_exp, u_exp, P, emd
        
        gc.collect()
        torch.cuda.empty_cache()
        
        return res