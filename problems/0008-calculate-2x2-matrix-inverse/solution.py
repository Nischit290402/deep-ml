import numpy as np
def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    a = np.array(matrix)
    det = a[0,0]*a[1,1] - a[0,1]*a[1,0]
    if det == 0:
        return None
    inv = 1.0/det
    adj = np.array([
        [a[1,1],-a[0,1]],
        [-a[1,0],a[0,0]]
        ])
    res = (1.0 / det) * adj
    res = np.round(res,5)
    return res.tolist()
    pass