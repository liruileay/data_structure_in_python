"""通过有序数组生成平衡搜索二叉树
	题目:给定一个有序数组sortARR,已知其中没有重复值,用这份有序数组生成一颗平和搜索二叉树,并且该搜索二叉树中序遍历的结果与sortArr一致
	
"""


class Node:
	def __init__(self, value):
		self.left = None
		self.right = None
		self.value = value


def generate(sort_arr, start, end):
	"""生成平衡二叉树的具体实现"""
	if start > end:
		return None
	mid = (start + end) // 2
	head = Node(sort_arr(mid))
	head.left = generate(sort_arr, start, mid - 1)
	head.right = generate(sort_arr, mid + 1, end)
	return head


def generate_tree(sort_arr):
	"""通过有序数组生成平衡二叉树"""
	if sort_arr is None:
		return None
	return generate(sort_arr, 0, len(sort_arr) - 1)
