def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	if not a or len(a[0]) != len(b):
		return -1

	result = []

	for i in range(len(a)):
		sum = 0
		for j in range(len(a[0])):
			sum += a[i][j]*b[j]
		result.append(sum)

	return result