import math

# 基于分治法的python列表归并排序
import time


def merge(src, result, start, inc):
	"""将src[stat:start+inc]和src[start+inc:start+2*inc]归并到result中"""
	end1 = start + inc
	end2 = min(start + 2 * inc, len(src))
	x, y, z = start, start + inc, start
	while x < end1 and y < end2:
		if src[x] < src[y]:
			result[z] = src[x]
			x += 1
		else:
			result[z] = src[y]
			y += 1
		z += 1
	if x < end1:
		result[z:end2] = src[x:end1]
	elif y < end2:
		result[z:end2] = src[y:end2]


def merge_sort(S):
	"""用python中的列表存储元素进行归并排序
	ceil:           取大于等于x的最小的整数值如果x是一个整数返回x
	log:            log(n,2) -->log(n)/log(2) ==>log2N
	
	"""
	n = len(S)
	logn = math.ceil(math.log(n, 2))
	src, dest = S, [None] * n
	for i in (2 ** k for k in range(logn)):
		for j in range(0, n, 2 * i):
			merge(src, dest, j, i)
		src, dest = dest, src
	if S is not src:
		S[0:n] = src[0:n]
