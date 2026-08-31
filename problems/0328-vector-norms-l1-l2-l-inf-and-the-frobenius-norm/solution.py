import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.
    
    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', or 'frobenius')
    
    Returns:
        The computed norm as a float
    """
    # Your code here
    arr = np.asarray(arr)

    if norm_type == 'l1':
        return float(np.sum(np.abs(arr)))
    elif norm_type in ('l2', 'frobenius'):
        return float(np.sqrt(np.sum(arr ** 2)))
    else:
        return ValueError(f"Unsupported norm_type: {norm_type}")
    pass