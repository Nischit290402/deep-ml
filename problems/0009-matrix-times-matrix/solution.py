import numpy as np
def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    A = np.array(a, dtype=float)
    B = np.array(b, dtype=float)
    try:
        c = A @ B
        return c.tolist()
    except ValueError:
        return -1