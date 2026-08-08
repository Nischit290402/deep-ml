import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	np_arr = np.array(a)
	if np_arr.size != (new_shape[0]*new_shape[1]):
		return []
	reshaped_np_matrix = np.reshape(a, new_shape)
	reshaped_matrix  = reshaped_np_matrix.tolist()
	return reshaped_matrix