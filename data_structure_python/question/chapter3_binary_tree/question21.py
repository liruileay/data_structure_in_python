"""
二叉树节点间的最大距离问题
	题目: 从二叉树的节点A出发,可以向上或者向下走,但沿途的节点只能经过一次,当到达节点B是,路径上的节点树叫做A到B的距离、
"""


def pos_order(head, record):
	if head is None:
		return 0
	lMax = pos_order(head.left, record)
	max_from_left = record[0]
	rmax = pos_order(head.right, record)
	max_from_right = record[0]
	cur_node_max = max_from_left + max_from_right + 1
	record[0] = max(max_from_right, max_from_left)
	return max(max(lMax, rmax), cur_node_max)


def max_distance(head):
	'''二叉树节点的最大距离'''
	record = [0]
	return pos_order(head, record)
