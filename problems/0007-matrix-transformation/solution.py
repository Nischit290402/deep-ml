import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	a = np.array(A, dtype=float)
	t = np.array(T, dtype=float)
	s  = np.array(S, dtype=float)
	try:
		ti = np.linalg.inv(t)
		_ = np.linalg.inv(s)
		R = ti @ a @ s
	except np.linalg.LinAlgError:
		return -1
	except e:
		return -1
	return R