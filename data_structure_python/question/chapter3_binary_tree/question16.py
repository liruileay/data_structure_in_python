"""
判断一棵树是否是搜索二叉树或者和完全二叉树
	题目: 给定一颗二叉树的头节点head,已知其中没有重复值的节点,实现两个函数分别判断这颗二叉树是否是搜索二叉树和完全二叉树
"""
from development.chapter6.ArrayQueue import ArrayQueue


class Node:
	
	def __init__(self, value):
		self.left = None
		self.right = None
		self.value = value


def isBST(head):
	'''通过morris中序遍历来判断是不是搜索二叉树'''
	if head is None:
		return True
	res = True
	pre = None
	cur1 = head
	while cur1 is not None:
		cur2 = cur1.left
		if cur2 is not None:
			while cur2.right is not None and cur2.right is not cur1:
				cur2 = cur2.right
			if cur2.right is None:
				cur2.right = cur1
				cur1 = cur1.left
			else:
				cur2.right = None
		if pre is not None and pre.value > cur1.value:
			res = False
		pre = cur1
		cur1 = cur1.right
	return res


def isCBT(head):
	'''判断二叉树是不是完全二叉树'''
	if head is None:
		return True
	queue = ArrayQueue()
	leaf = False
	queue.enqueue(head)
	while not queue.is_empty():
		head = queue.dequeue()
		l = head.left
		r = head.right
		if (leaf and (l is not None or r is not None) or (l is None and r is not None)):
			return False
		if l is not None:
			queue.enqueue(l)
		if r is not None:
			queue.enqueue(r)
		else:
			leaf = True
	return True
