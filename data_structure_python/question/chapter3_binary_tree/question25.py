"""
统计完全二叉树的节点个数
	要求实现事件复杂度为O（N）的算法
"""


def bs(node, l, h):
	if l == h:
		return 1
	if most_left_level(node.right, l + 1) == h:
		return (1 << (h - 1)) + bs(node.right, l + 1, h)
	else:
		return (1 << (h - l - 1)) + bs(node.left, l + 1, h)


def most_left_level(node, level):
	while node is not None:
		level += 1
		node = node.left
	return level - 1


def node_num(head):
	"""统计完全二叉树的个数"""
	if head is None:
		return None
	return bs(head, 1, most_left_level(head, 1))
