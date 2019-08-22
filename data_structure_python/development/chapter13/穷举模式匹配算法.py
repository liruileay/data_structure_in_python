def find_brute(T, P):
	"""从T中匹配P并且如果匹配到了就返回P中第一个字母在T中的索引如果没有匹配成功返回-1"""
	n, m = len(T), len(P)
	for i in range(n - m + 1):
		k = 0
		while k < m and P[k] == T[k + i]:
			k += 1
		if k == m:
			return i
	return -1