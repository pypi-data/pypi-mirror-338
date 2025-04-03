from scipy.spatial import cKDTree
import numpy as np
import torch
import torch.nn as nn
import gc
from typing import Tuple

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def k_nearest_neighbors(x: np.ndarray, 
                        y: np.ndarray, 
                        k: int = 1,
                        squared_distances: bool = False,
                        max_points_per_leaf: int = 10) -> Tuple[np.ndarray, np.ndarray]:
    """
    Compute k-nearest neighbors between batched point clouds.
    
    Args:
        x: Query points (m, n_a, d)
        y: Reference points (m, n_b, d) 
        k: Number of nearest neighbors
        squared_distances: Return squared distances if True
        max_points_per_leaf: KD-tree leaf size parameter
    
    Returns:
        Tuple of (distances, indices):
        - distances: (m, n_a, k) array of distances
        - indices: (m, n_a, k) array of indices into y
    """
    if x.ndim != 3 or y.ndim != 3:
        raise ValueError("Inputs must be 3D arrays (batch, points, dim)")
    if x.shape[0] != y.shape[0]:
        raise ValueError("Batch size mismatch between x and y")
    if x.shape[2] != y.shape[2]:
        raise ValueError("Dimension mismatch between x and y")

    batch_size = x.shape[0]
    all_dists = np.empty((batch_size, x.shape[1], k))
    all_indices = np.empty((batch_size, x.shape[1], k), dtype=int)

    for i in range(batch_size):
        tree = cKDTree(y[i], leafsize=max_points_per_leaf)
        dists, indices = tree.query(x[i], k=k)
        
        if k == 1:
            dists = dists[:, None]
            indices = indices[:, None]

        all_dists[i] = dists**2 if squared_distances else dists
        all_indices[i] = indices

    return all_dists, all_indices

def chamfer_distance(x: np.ndarray, 
                     y: np.ndarray, 
                     return_index: bool = False, 
                     p_norm: int = 2, 
                     max_points_per_leaf: int = 10) -> float:
    dists_x_to_y, corrs_x_to_y = k_nearest_neighbors(x, y, k=1, 
                                                    max_points_per_leaf=max_points_per_leaf)
    dists_y_to_x, corrs_y_to_x = k_nearest_neighbors(y, x, k=1,
                                                    max_points_per_leaf=max_points_per_leaf)

    # 修正索引方式
    batch_dists_x = []
    for i in range(x.shape[0]):
        matched_y = y[i][corrs_x_to_y[i][:, 0]]  # 正确索引当前batch的点
        batch_dists = np.linalg.norm(x[i] - matched_y, axis=-1, ord=p_norm)
        batch_dists_x.append(batch_dists.mean())

    batch_dists_y = []
    for i in range(y.shape[0]):
        matched_x = x[i][corrs_y_to_x[i][:, 0]]  # 正确索引当前batch的点
        batch_dists = np.linalg.norm(y[i] - matched_x, axis=-1, ord=p_norm)
        batch_dists_y.append(batch_dists.mean())

    cham_dist = (np.mean(batch_dists_x) + np.mean(batch_dists_y)) / 2

    if return_index:
        return cham_dist, corrs_x_to_y, corrs_y_to_x
    return cham_dist




# ----------------- Chamfer Distance -----------------
def chamfer_distance_gpu(p1: torch.Tensor, 
                    p2: torch.Tensor, 
                    p_norm: int = 2,
                    reduce_mean: bool = True) -> torch.Tensor:
    """
    Batched Chamfer Distance with GPU acceleration
    Args:
        p1: (B, N, D) tensor
        p2: (B, M, D) tensor
        p_norm: norm type (1 or 2)
        reduce_mean: whether to average over batch
    Returns:
        (B,) tensor of chamfer distances or scalar if reduce_mean=True
    """
    # 计算成对距离矩阵
    dist = torch.cdist(p1, p2, p=p_norm)  # (B, N, M)
    
    # 双向最近邻距离
    min_dist_p1_to_p2, _ = torch.min(dist, dim=2)  # (B, N)
    min_dist_p2_to_p1, _ = torch.min(dist, dim=1)  # (B, M)
    
    # 聚合结果
    cost_p1 = torch.mean(min_dist_p1_to_p2, dim=1)  # (B,)
    cost_p2 = torch.mean(min_dist_p2_to_p1, dim=1)
    total_cost = (cost_p1 + cost_p2) / 2.0
    res = torch.mean(total_cost) if reduce_mean else total_cost
    
    del dist, min_dist_p1_to_p2, min_dist_p2_to_p1, cost_p1, cost_p2, total_cost
    gc.collect()
    torch.cuda.empty_cache()
    return res

    