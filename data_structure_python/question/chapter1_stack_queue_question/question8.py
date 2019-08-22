"""
题目：
	有一个整型数组arr和一个大小为w的窗口从数组中的最左边滑到最右边，窗口每次向右边滑一个位置
	例如,         数组[4,3,5,4,3,3,6,7]
	[4,3,5],4,3,3,6,7       最大值是5
	4,[3,5,4],3,3,6,7       最大值是5
	4,3,[5,4,3],3,6,7       最大值是5
	4,3,5,[4,3,3],6,7       最大值是4
	4,3,5,4,[3,3,6],7       最大值是6
	4,3,5,4,3,[3,6,7]       最大值是7
"""
from development.chapter6.Double_ArrayQueue import DoubleArrayQueue


def get_max_window(arr, w):
	"""每次弹出的逻辑实现"""
	if len(arr) < w or w < 1:
		return
	Qmax = DoubleArrayQueue()
	res = [0] * (len(arr) - w + 1)
	index = 0
	for i in range(len(arr)):
		while not Qmax.is_empty() and arr[Qmax.last()] <= arr[i]:
			Qmax.delete_last()
		Qmax.add_last(i)
		if Qmax.first() == i - w:
			Qmax.delete_first()
		if i >= w - 1:
			res[index] = arr[Qmax.first()]
			index += 1
	return res


if __name__ == '__main__':
	get_max_window([4, 3, 5, 4, 3, 3, 6, 7], 3)
