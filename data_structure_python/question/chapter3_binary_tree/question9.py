"""
找到二叉树中符合搜索二叉树条件的最大拓扑结构
	题目:给定一个二叉树的头节点head,已知所有节点的值都是不一样的,
		返回其中最大的且符合搜索二叉树条件的最大拓扑结构的大小
"""
from development.chapter10.ChainHashMap import ChainHashMap


class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None


class BstTopoSize1(object):
	"""方法一"""
	
	def is_BST_node(self, h, n, value):
		if h is None:
			return False
		if h == n:
			return True
		return self.is_BST_node(h.left if h.value > value else h.right, n, value)
	
	def max_topo(self, h, n):
		if h is not None and n is not None and self.is_BST_node(h, n, n.value):
			return self.max_topo(h, n.left) + self.max_topo(h, n.right) + 1
		return 0
	
	def bst_topo_size1(self, head):
		'''返回搜索二叉树条件的最大拓扑结构实现1'''
		if head is None:
			return 0
		max = self.max_topo(head, head)
		max = max(self.bst_topo_size1(head.left), max)
		max = max(self.bst_topo_size1(head.right), max)
		return max


class BstTopoSize2(object):
	"""方法二"""
	
	class Record:
		def __init__(self, left, right):
			self.l = left
			self.r = right
	
	def modify_map(self, n, v, m, s):
		if n is None or not m.__contains__(n):
			return 0
		r = m[n]
		if (s and n.value > v) or ((not s) and n.value < v):
			m.pop(n)
			return r.l + r.r + 1
		else:
			minus = self.modify_map(n.right if s else n.left, v, m, s)
			if s:
				r.r = r.r - minus
			else:
				r.l = r.l - minus
			m[n] = r
			return minus
	
	def pos_order(self, h, map):
		if h is None:
			return 0
		ls = self.pos_order(h.left, map)
		rs = self.pos_order(h.right, map)
		self.modify_map(h.left, h.value, map, True)
		self.modify_map(h.right, h.value, map, False)
		lr = map[h.left]
		rr = map[h.right]
		lbst = 0 if lr is None else lr.l + lr.r + 1
		rbst = 0 if rr is None else rr.l + rr.r + 1
		map[h] = self.Record(lbst, rbst)
		return max(lbst + rbst + 1, max(ls, rs))
	
	def bst_topo_size2(self, head):
		"""返回搜索二叉树条件的最大拓扑结构"""
		map = ChainHashMap()
		return self.pos_order(head, map)
