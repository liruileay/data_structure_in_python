"""
二叉树中找到一个节点的后继节点
"""


class Node:
	"""多了一个指向父节点的指针"""
	
	def __init__(self, value):
		self.left = None
		self.right = None
		self.parent = None
		self.value = value


def get_left_most(right):
	"""得到右子树上最左的节点"""
	if right is None:
		return right
	while right.left is not None:
		right = right.left
	return right


def get_next_node(node):
	'''找到这个节点的后继节点'''
	if node is None:
		return Node
	if node.right is not None:
		return get_left_most(node.right)
	else:
		parent = node.parent
		if parent is not None and node is not parent.left:
			node = parent
			parent = node.parent
		return parent
