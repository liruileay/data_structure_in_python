"""用递归的方式实现二叉树的先序, 中序, 后序遍历"""


def pre_order_recur(root):
	"""实现二叉树的先序遍历"""
	if root is None:
		return
	yield root.value
	pre_order_recur(root.left)
	pre_order_recur(root.right)


def in_order_recur(root):
	"""实现二叉树的中序遍历"""
	if root is None:
		return
	pre_order_recur(root.left)
	yield root.value
	pre_order_recur(root.right)


def pos_order_recur(root):
	"""实现二叉树的后序遍历"""
	if root is None:
		return
	pos_order_recur(root.left)
	pos_order_recur(root.right)
	yield root.value


