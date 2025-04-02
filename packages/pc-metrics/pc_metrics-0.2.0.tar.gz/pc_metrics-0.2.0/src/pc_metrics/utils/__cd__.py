from scipy.spatial import cKDTree
import numpy as np
from typing import Tuple

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
    """
    Compute Chamfer distance between batched point clouds.
    
    Args:
        x: Query point clouds (m, n_a, d)
        y: Reference point clouds (m, n_b, d)
        return_index: Return correspondence indices if True
        p_norm: Norm for distance calculation
        max_points_per_leaf: KD-tree leaf size parameter
    
    Returns:
        Chamfer distance (float) or tuple with correspondences
    """
    dists_x_to_y, corrs_x_to_y = k_nearest_neighbors(x, y, k=1, 
                                                    max_points_per_leaf=max_points_per_leaf)
    dists_y_to_x, corrs_y_to_x = k_nearest_neighbors(y, x, k=1,
                                                    max_points_per_leaf=max_points_per_leaf)

    dists_x_to_y = np.linalg.norm(x - y[corrs_x_to_y], axis=-1, ord=p_norm).mean()
    dists_y_to_x = np.linalg.norm(y - x[corrs_y_to_x], axis=-1, ord=p_norm).mean()

    cham_dist = dists_x_to_y + dists_y_to_x

    if return_index:
        return cham_dist, corrs_x_to_y, corrs_y_to_x
    return cham_dist