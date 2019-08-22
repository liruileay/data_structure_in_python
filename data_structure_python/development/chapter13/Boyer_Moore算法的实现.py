# 基于Boyer-Moore算法实现
def find_boyer_moore(T, P):
	"""如果在T中匹配到了P那么返回P中的第一个元素在T中的索引如果没有匹配D到就返回-1"""
	# 如果P中的任何位置都不包含c，则将P完全移动到T[i]后面 因为他不能匹配P中的任何一个字符
	# 直到P中出现字符c并与T[i]一致才能移动P
	n, m = len(T), len(P)
	if m == 0: return 0
	last = {}
	for k in range(m):
		last[P[k]] = k  # 记录P中每一元素的最大index
	i = m - 1
	k = m - 1
	while i < n:
		if P[k] == T[i]:
			if k == 0:
				return i
			else:
				k -= 1
				i -= 1
		else:
			j = last.get(T[i], -1)
			i += m - min(k, j + 1)
			k = m - 1
	return -1
