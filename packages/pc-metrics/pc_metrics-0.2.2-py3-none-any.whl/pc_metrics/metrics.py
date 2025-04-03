import numpy as np
from sklearn.neighbors import NearestNeighbors
from scipy.stats import entropy
from .utils import chamfer_distance,earth_movers_distance, chamfer_distance_gpu, EMDLoss
from typing import Tuple, List
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def CD(p1: np.ndarray, p2: np.ndarray, gpu: bool = True) -> float:
    """Chamfer Distance between single point clouds."""
    if not gpu:
        return chamfer_distance(p1, p2)
    p1_t = torch.from_numpy(p1).float().to(device).unsqueeze(0)
    p2_t = torch.from_numpy(p2).float().to(device).unsqueeze(0)
    return chamfer_distance_gpu(p1_t, p2_t).item()

def EMD(p1: np.ndarray, p2: np.ndarray, gpu: bool=True) -> float:
    """Earth Mover's Distance between single point clouds."""
    if not gpu:
        earth_movers_distance(p1, p2)
    emd_loss = EMDLoss()
    p1_t = torch.from_numpy(p1).float().to(device).unsqueeze(0)
    p2_t = torch.from_numpy(p2).float().to(device).unsqueeze(0)
    return emd_loss(p1_t, p2_t).item()

def MMD(sample_pcs: np.ndarray, 
       ref_pcs: np.ndarray, 
       use_emd: bool = False) -> float:
    """Minimum Matching Distance between point cloud sets."""
    metric = EMD if use_emd else CD
    return np.mean([np.min([metric(ref_pc, s) for s in sample_pcs]) for ref_pc in ref_pcs])

def Coverage(sample_pcs: np.ndarray, 
            ref_pcs: np.ndarray, 
            use_emd: bool = False) -> Tuple[float, List[int]]:
    """Coverage metric for generated point clouds."""
    matched = [np.argmin([EMD(s, r) if use_emd else CD(s, r) for r in ref_pcs]) 
              for s in sample_pcs]
    return len(np.unique(matched))/len(ref_pcs), matched

def JSD(sample_pcs: np.ndarray, 
       ref_pcs: np.ndarray, 
       resolution: int = 28) -> float:
    """Jensen-Shannon Divergence between point cloud distributions."""
    def entropy_grid(pcs):
        grid = np.linspace(-0.5, 0.5, resolution)
        grid_pts = np.stack(np.meshgrid(grid, grid, grid), -1).reshape(-1, 3)
        nn = NearestNeighbors(n_neighbors=1).fit(grid_pts)
        counts = np.zeros(len(grid_pts))
        for pc in pcs:
            counts[np.unique(nn.kneighbors(pc.reshape(-1, 3))[1])] += 1
        prob = np.clip(counts/len(pcs), 1e-10, 1.0)
        return entropy(prob, base=2)
    
    p = entropy_grid(sample_pcs)
    q = entropy_grid(ref_pcs)
    m = 0.5 * (p + q)
    return 0.5 * (entropy(p, m) + entropy(q, m))