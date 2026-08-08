def calculate_matrix_mean(a: list[list[float]], mode: str) -> list[float]:
	means = []
	
	if mode == "row":
		flag = True
		n = len(a)
		m = len(a[0])
	elif mode == "column":
		flag = False
		m = len(a)
		n = len(a[0])
		
	for i in range(n):
		sum = 0
		for j in range(m):
			if flag: 
				sum += a[i][j]
			else:
				sum += a[j][i]
		sum /= m
		means.append(sum)

	return means