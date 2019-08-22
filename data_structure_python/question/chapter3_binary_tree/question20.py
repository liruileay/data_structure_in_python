"""
Tarjan算法与并查集解决二叉树节点间最近公共祖先的批量查询问题
	题目:
"""
from development.chapter10.ChainHashMap import ChainHashMap
from development.chapter7.FavoritesList import FavoritesList as LinkedList


class Node:
	
	def __init__(self, value):
		self.left = None
		self.right = None
		self.value = value


class Query:
	
	def __init__(self, o1, o2):
		self.o1 = o1
		self.o2 = o2


# 要求如果二叉树的节点个数为N,查询语句的条数为M,整个处理过程的时间复杂度要求达到O(N+M)

class DisjointSets:
	
	def __init__(self):
		self.father_map = ChainHashMap()
		self.rank_map = ChainHashMap()
	
	def make_set(self, node):
		self.father_map.clear()
		self.rank_map.clear()
		self.pre_order_make(node)
	
	def pre_order_make(self, head):
		if head is None:
			return
		self.father_map[head] = head
		self.rank_map[head] = 0
		self.pre_order_make(head.left)
		self.pre_order_make(head.right)
	
	def find_father(self, n):
		father = self.father_map.get(n)
		if father is not n:
			father = self.find_father(father)
		self.father_map[n] = father
		return father
	
	def union(self, a, b):
		if a is None or b is None:
			return
		a_father = self.find_father(a)
		b_father = self.find_father(b)
		if a_father is not b_father:
			a_frank = self.rank_map.get(a_father)
			b_frank = self.rank_map.get(b_father)
			if a_frank < b_frank:
				self.father_map[a_father] = b_father
			elif a_frank > b_frank:
				self.father_map[b_father] = a_father
			else:
				self.father_map[b_father] = a_father
				self.rank_map[a_father] = a_frank + 1


class Tarjan(object):
	
	def __init__(self):
		self.query_map = ChainHashMap()
		self.index_map = ChainHashMap()
		self.ancestor_map = ChainHashMap()
		self.sets = DisjointSets()
	
	def query(self, head, ques):
		ans = [None] * len(ques)
		self.set_queries(ques, ans)
		self.sets.make_set(head)
		self.set_answers(head, ans)
		return ans
	
	def set_queries(self, ques, ans):
		for i in range(len(ans)):
			o1 = ques[i].o1
			o2 = ques[i].o2
			if o1 is o2 or o1 is None or o2 is None:
				ans[i] = o1 if o1 is not None else o2
			else:
				if not self.query_map.__contains__(o1):
					self.query_map[o1] = LinkedList()
					self.index_map[o1] = LinkedList()
				if not self.query_map.__contains__(o2):
					self.query_map[o2] = LinkedList()
					self.index_map[o2] = LinkedList()
				self.query_map.get(o1).access(o2)
				self.index_map.get(o1).access(i)
				self.query_map.get(o2).access(o1)
				self.index_map.get(o2).access(i)
	
	def set_answers(self, head, ans):
		if head is None:
			return
		self.set_answers(head.left, ans)
		self.sets.union(head.left, head)
		self.ancestor_map[self.sets.find_father(head)] = head
		self.set_answers(head.right, ans)
		self.sets.union(head.right, head)
		self.ancestor_map[self.sets.find_father(head)] = head
		nList = self.query_map.get(head)
		iList = self.index_map.get(head)
		while nList is not None and not nList.is_empty():
			node = nList.pop()
			index = iList.pop()
			node_father = self.sets.find_father(node)
			if self.ancestor_map.__contains__(node):
				ans[index] = self.ancestor_map.get(node_father)
