import numpy as np
def calculate_eigenvalues(a: list[list[float|int]]) -> list[float]:
	trace = a[0][0]+a[1][1]
	det = a[0][0]*a[1][1]-a[0][1]*a[1][0]
	D = np.sqrt(trace*trace - 4*det)
	eigenvalues = []
	eigenvalues.append((trace+D)/2)
	eigenvalues.append((trace-D)/2)
	return eigenvalues