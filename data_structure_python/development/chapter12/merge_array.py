# 基于分治法的python数组的归并排序实现
def merge(S1, S2, S):
	"""数组S1有序S2有序将S1和S2中的按照大小替换到S中"""
	i = j = 0
	while i + j < len(S):
		if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
			S[i + j] = S1[i]
			i += 1
		else:
			S[i + j] = S2[j]
			j += 1


def merge_sort(S):
	"""归并排序的具体实现"""
	n = len(S)
	if n < 2:
		return
	mid = n // 2
	S1 = S[0:mid]
	S2 = S[mid:n]
	merge_sort(S1)
	merge_sort(S2)
	merge(S1, S2, S)
