"""
调整搜索二叉树中两个错误的节点
	题目:
		一颗二叉树原本是一颗搜索二叉树,但是其中有两个节点调换了位置,使得这颗二叉树的不再是搜索二叉树,
		请找出这两个错误的节点并返回。已知一颗二叉树中所有节点的值都是给定二叉树的头节点head,返回一个长度为2
		的二叉树的节点类型的数组errs,errs[0]表示一个错误几点errs[1]表示另一个错误节点
	进阶:
		如果在原问题中得到了这两个错误节点,我们当然可以通过交换两个节点值的方式让整棵二叉树重新成为一个搜索二叉树
		,但是现在不能这样做,而是在结构上面完全交换这两个节点的位置,请实现调整函数
"""
from development.chapter6.ArrayStack import ArrayStack


class Node:
	
	def __init__(self, value):
		self.left = None
		self.right = None
		self.value = value


def get_twoerr_node(head):
	'''得到两个错误的节点'''
	errs = [None] * 2
	if head is None:
		return errs
	stack = ArrayStack()
	pre = None
	while not stack.is_empty() or head is not None:
		if head is not None:
			stack.push(head)
			head = head.left
		else:
			head = stack.pop()
			if pre is not None and pre.value > head.value:
				errs[0] = pre if errs[0] is None else errs[0]
				errs[1] = head
			pre = head
			head = head.right


def get_twoerr_parents(head, e1, e2):
	'''找到连个错误节点进行重连'''
	parents = [None] * 2
	if head is None:
		return parents
	stack = ArrayStack()
	while not stack.is_empty() or head is None:
		if head is not None:
			stack.push(head)
			head = head.left
		else:
			head = stack.pop()
			if head.left is e1 or head.right is e1:
				parents[0] = head
			if head.left is e2 or head.right is e2:
				parents[1] = head
			head = head.right
	return parents

