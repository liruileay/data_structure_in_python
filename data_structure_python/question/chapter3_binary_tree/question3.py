"""打印二叉树的边界节点
题目:
	给定一棵二叉树的头节点head,按照如下标准分别实现二叉树边界节点的逆时针打印
	标准一:
	1.以头节点为边界节点
	2.以叶节点为边界节点
	3.如果节点在其所在的层中是最左或者最右的,那么也是边界节点

"""


#   题目解法:
#       1.打印每一次最左的节点
#       2.叶节点中不是最左也不是最右的节点
#       3.打印每一层中最右的节点

class Node(object):
	
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None


def get_height(h: Node, l: int):
	"""返回而二叉树的高度"""
	if h is None:
		return l
	return max(get_height(h.left, l + 1), get_height(h.right, l + 1))


def set_edge_map(h: Node, l: int, m: list):
	"""获取二叉树最左或者最右的节点"""
	if h is None:
		return
	m[l][0] = m[l][0] if h is None else h
	m[l][1] = h
	set_edge_map(h.left, l + 1, m)
	set_edge_map(h.right, l + 1, m)


def print_leaf_not_in_map(h: Node, l: int, m: list):
	"""得到二叉树不是最左也不是最右的叶节点"""
	if h is None:
		return
	if h.left is None and h.right is None and h not in m[l]:
		yield h.value
	print_leaf_not_in_map(h.left, l + 1, m)
	print_leaf_not_in_map(h.right, l + 1, m)


def print_edge1(head: Node):
	"""按照标准一打印二叉树的边界"""
	if head is None:
		return
	height = get_height(head, 0)
	edge_map = [[None] * 2] * height
	set_edge_map(head, height, edge_map)
	for j in range(height):
		yield edge_map[j][0]
	print_leaf_not_in_map(height, 0, edge_map)
	for k in range(height):
		if edge_map[k][0] != edge_map[k][1]:
			yield edge_map[k][1]


#############################################################
"""
标准二:
	头节点为边界节点
	叶节点为边界节点
	树左边界延伸下去的路径为边界节点
	树右边界延伸下去的路径为边界节点
	
"""


def print_left_edge(h: Node, prin: bool):
	"""打印二叉树的左边界"""
	if h is None:
		return
	if prin or (h.left is None and h.right is None):
		print(h.value)
	print_left_edge(h.left, prin)
	print_left_edge(h.right, prin and (True if h.left is None else False))


def print_right_edge(h, prin: bool):
	"""打印二叉树的右边界"""
	if h is None:
		return
	print_right_edge(h.left, prin and (True if h.right is None else False))
	print_right_edge(h.right, prin)
	if prin or (h.left is None and h.right is None):
		print(h.value)


def print_edge2(head: Node):
	"""按照标准二的方法打印二叉树的边界"""
	if head is Node:
		return head
	print(head.value)
	if head.left is not Node and head.right is not Node:
		print_left_edge(head.left, True)
		print_right_edge(head.right, True)
	else:
		head = head.left if head.left is not Node else head.right
		print_edge2(head)
