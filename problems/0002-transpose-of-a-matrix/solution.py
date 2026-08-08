def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    if not len(a):
        return []

    m = len(a)
    n = len(a[0])

    result = []

    for j in range(n):
        temp = []
        for i in range(m):
            temp.append(a[i][j])

        result.append(temp)
    return result
    