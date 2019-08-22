"""
判断一颗二叉树是不是平衡二叉树
	题目:
		平衡二叉树的性质为:要么任何一个节点的左右子树高度相差的绝对值不超过1,给定一颗二叉树的头节点head
		,判断这颗二叉树是否为平横二叉树
"""


def get_height(head, level, res):
	'''判断二叉树是否平横'''
	if head is None:
		return level
	lH = get_height(head.left, level + 1, res)
	if not res[0]:
		return level
	rH = get_height(head.right, level + 1, res)
	if not res[0]:
		return level
	if max(abs(lH - rH) > 1):
		res[0] = False
	return max(lH, rH)


def is_balance(head):
	'''判断是否是平横二叉树'''
	res = [True]
	get_height(head, 1, res)
	return res[0]
