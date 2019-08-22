"""
根据后序数组重建二叉树

	给定一个整型数组 arr 已知其中没有重复值 判断arr是否可能是节点值类型为整型的搜索二叉树后序遍历的结果
	进阶: 如果整型数组arr中没有重复值 且已知是一颗搜索二叉树的后序遍历结果通过数组arr重构二叉树
	
"""


def is_post(arr, start, end):
	'''判断数组是不是搜索二叉树的后序遍历数组'''
	# 数组的头节点在数组的最后一个元素 比数组最后一个元素小的在左边 比数组最后一个元素大的在右边
	if start == end:
		return True
	less = -1
	more = end
	for i in range(start, end):
		if arr[end] > arr[i]:
			less = i
		else:
			more = i if more == end else more
	if less == -1 or more == end:  # 表示没有左孩子或者没有右孩子
		return is_post(arr, start, end - 1)
	if less != more - 1:  # 表示中间右满足条件的
		return False
	return is_post(arr, start, less) and is_post(arr, more, end - 1)


class Node:
	def __init__(self, value):
		self.left = None
		self.right = None
		self.value = value


def is_pos_array(arr):
	'''判断arr是不是搜索二叉树的后序遍历'''
	if arr is None or len(arr) == 0:
		return False
	return is_post(arr, 0, len(arr) - 1)


def pos_to_BST(pos_arr, start, end):
	'''重构的逻辑实现'''
	if start > end:
		return None
	head = Node(pos_arr[end])
	less = -1
	more = end
	for i in range(start, end):
		if pos_arr[end] > pos_arr[i]:
			less = i
		else:
			more = i if more == end else more
	head.left = pos_to_BST(pos_arr, start, less)
	head.right = pos_to_BST(pos_arr, more, end - 1)
	return head


def pos_array_to_BST(pos_arr):
	'''已知是一颗搜索二叉树的后序遍历将其序列化'''
	if pos_arr is None:
		return None
	return pos_to_BST(pos_arr, 0, len(pos_arr) - 1)
