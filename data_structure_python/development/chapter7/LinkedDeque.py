from development.chapter6.ArrayQueue import Empty
from development.chapter7._DoublyLinkBase import _DoublyLinkedBase


class LinkedDeque(_DoublyLinkedBase):
	"""链表实现双端队列"""
	
	def first(self):
		"""查看第一个元素"""
		if self.is_empty():
			raise Empty("Deque is empty")
		return self._header._next._element
	
	def last(self):
		"""查看最后一个元素"""
		if self.is_empty():
			raise Empty("Deque is empty")
		return self._trailer._prev._element
	
	def insert_first(self, e):
		"""从头插入"""
		self._insert_between(e, self._header, self._header._next)
	
	def insert_last(self, e):
		"""从尾部插入"""
		self._insert_between(e, self._trailer._prev, self._trailer)
	
	def delete_first(self):
		"""删除头节点"""
		if self.is_empty():
			raise Empty("Deque is empty")
		self._delete_node(self._header._next)
	
	def delete_last(self):
		"""删除尾节点"""
		if self.is_empty():
			raise Empty("Deque is empty")
		self._delete_node(self._trailer._prev)
