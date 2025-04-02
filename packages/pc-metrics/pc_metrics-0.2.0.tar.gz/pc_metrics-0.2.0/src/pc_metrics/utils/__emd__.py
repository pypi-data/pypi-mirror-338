import numpy as np


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