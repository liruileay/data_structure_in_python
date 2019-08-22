def line_sum(S, n):
	if n == 0:
		return n
	return line_sum(S, n - 1) + S[n - 1]


