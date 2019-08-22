"""
最大值减去最小值小于或者等于num的子数组数量
题目:
	给定数组arr和整数num,共返回有多少个子数组满足如下情况:
		max(arr[i..j]) - min(arr[i..j]) <=num
		max(arr[i..j]}表示子数组arr[i..j]中的最大值,min(arr[i..j])表示子数组arr[i..j]中的最小值
要求:
	如果数组的长度为N,请实现时间复杂度为O(N)的解法
"""
from development.chapter7.LinkedDeque import LinkedDeque


def get_num(arr, num):
	"""最大值减去最小值等于num的数量的具体实现"""
	if len(arr) == 0 or num is None:
		return
	qmin = LinkedDeque()
	qmax = LinkedDeque()
	i, j, res = 0, 0, 0
	while i < len(arr):
		while j < len(arr):
			"""一个递增的栈元素"""
			while not qmin.is_empty() and arr[qmin.last()] >= arr[j]:
				qmin.delete_last()
			qmin.insert_last(j)
			"""一个递减的栈元素"""
			while not qmax.is_empty() and arr[qmax.last()] <= arr[j]:
				qmax.delete_last()
			qmax.insert_last(j)
			if arr[qmax.first()] - arr[qmin.first()] > num:
				break
			j += 1
		if qmin.first() == i:
			qmin.delete_first()
		if qmax.first() == i:
			qmax.delete_first()
		res += j - i
		i += 1
	return res


if __name__ == '__main__':
	num = get_num([6, 3, 9, 17, 9], 10)
	print(num)
