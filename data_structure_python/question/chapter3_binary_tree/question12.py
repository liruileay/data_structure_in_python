"""
判断t1树是否包含t2树的全部拓扑结构
	题目: 给定彼此独立的两颗树头节点分别为t1和t2,判断t1树是否包含t2树的全部拓扑结构
	
"""


def check(h, t2):
	'''判断t1是否包含t2的全部拓扑结构'''
	if t2 is None:
		return True
	if h is None or h.value != t2.value:
		return False
	return check(h.left, t2.left) and check(h.right, t2.right)


def contains(t1, t2):
	'''判断t1是否包含t2的全部拓扑结构'''
	return check(t1, t2) or contains(t1.left, t2) or contains(t1.right, t2)

