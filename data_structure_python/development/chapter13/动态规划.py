def matrix_chain(d):
	"""矩阵链乘积的动态规划算法"""
	n = len(d) - 1
	N = [[0] * n for i in range(n)]
	for b in range(1, n):
		for i in range(n - b):
			j = i + b
			N[i][j] = min(N[i][k] + N[k + 1][j] + d[i] * d[k + 1] * d[j + 1] for k in range(i, j))
	return N

print(matrix_chain("fgdfgdgeegrggdfgdgrer"))

def LCS(X, Y):
	"LCS问题的动态规划算法"
	n, m = len(X), len(Y)
	L = [[0] * (m + 1) for k in range(n + 1)]
	for j in range(n):
		for k in range(m):
			if X[j] == Y[k]:
				L[j + 1][k + 1] = L[j][k] + 1
			else:
				L[j + 1][k + 1] = max(L[j][k + 1], L[j + 1][k])
	return L


def LCS_solution(X, Y, L):
	"""最长公共子序列的重建"""
	solution = []
	j, k = len(X), len(Y)
	while L[j][k] > 0:
		if X[j - 1] == Y[k - 1]:
			solution.append(X[j - 1])
			j -= 1
			k -= 1
		elif L[j - 1][k] >= L[j][k - 1]:
			j -= 1
		else:
			k -= 1
	return ''.join(reversed(solution))
