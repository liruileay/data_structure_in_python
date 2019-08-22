def compute_kmp_fail(P):
	"""用于记录匹配失败后P对应的位移"""
	"""
	失败函数用于记录子串的最长前缀
				其中aba的最长前缀是 a长度是1
				aaa的最长前缀是    aa 长度是2
	
	"""
	m = len(P)
	fail = [0] * m
	j = 1
	k = 0
	while j < m:
		if P[j] == P[k]:
			fail[j] = k + 1
			j += 1
			k += 1
		elif k > 0:
			k = fail[k - 1]
		else:
			j += 1
	return fail


def find_kmp(T, P):
	"""KMP模式匹配算法的实现 ---->只能匹配到第一个子串"""
	n, m = len(T), len(P)
	if m == 0: return 0
	fail = compute_kmp_fail(P)
	j = 0
	k = 0
	while j < n:
		if T[j] == P[k]:
			if k == m - 1:
				return j - m + 1
			else:
				j += 1
				k += 1
		elif k > 0:
			k = fail[k - 1]
		else:
			j += 1
	return -1

a = "dfsdfdsfs"
print(a[1])