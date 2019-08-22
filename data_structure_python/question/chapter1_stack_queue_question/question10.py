"""
求最大子矩阵的大小
	给定的一个整型的矩阵map,其中值只有0和1两个,求全是1的所有矩阵区域中,最大的矩阵区域数量
	1   0   1   1
	1   1   1   1
	1   1   1   0
	这个矩阵的最大矩阵区域数量是6 那么返回6
"""
from development.chapter6.ArrayStack import ArrayStack


def max_rec_from_bottom(height):
	"""找出以每一层为底切出来的最大子矩阵的大小"""
	if len(height) == 0 or height is None:
		return 0
	max_area = 0
	stack = ArrayStack()
	for i in range(len(height)):
		while not stack.is_empty() and height[i] <= height[stack.top()]:
			j = stack.pop()
			k = -1 if stack.is_empty() else stack.top()
			cur_area = (i - k - 1) * height[j]
			max_area = max(cur_area, max_area)
		stack.push(i)
	while not stack.is_empty():
		j = stack.pop()
		k = -1 if stack.is_empty() else stack.top()
		cur_area = (len(height) - k - 1) * height[j]
		max_area = max(cur_area, max_area)
	return max_area


def max_rec_size(arr_map):
	"""返回最大子矩阵数量的具体实现"""
	if len(arr_map) < 1 or len(arr_map[0]) < 1:
		return 0
	max_area = 0
	height = [0] * len(arr_map[0])
	for i in range(len(arr_map)):
		for j in range(len(arr_map[0])):
			height[j] = 0 if arr_map[i][j] == 0 else height[j] + 1
		max_area = max(max_rec_from_bottom(height), max_area)
	return max_area


if __name__ == '__main__':
	max_size = max_rec_size([[1, 0, 1, 1],
	                         [1, 1, 1, 1],
	                         [1, 1, 1, 0]])
	print(max_size)
