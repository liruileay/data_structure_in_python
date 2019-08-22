from development.chapter6.ArrayQueue import Empty


class LinkedQueue(object):
	"""链表实现一个队列每从队列顶部弹出一个数"""
	class _Node:
		__slots__ = '_element', '_next'
		
		def __init__(self, element, next):
			self._element = element
			self._next = next
	
	def __init__(self):
		"""初始化链表的头节点位置和链表的尾部节点(哨兵节点)"""
		self._head = None
		self._size = 0
		self._tail = None
	
	def is_empty(self):
		'''判断该栈是否为空'''
		return self._size == 0
	
	def __len__(self):
		'''返回栈的长度'''
		return self._size
	
	def first(self):
		"""查看链表头节点的元素"""
		if self.is_empty():
			raise Empty("Queue is empty")
		return self._head._element()
	
	def dequeue(self):
		"""从头节点弹出一个元素"""
		if self.is_empty():
			raise Empty("Queue is empty")
		answer = self._head._element
		self._head = self._head._next
		self._size -= 1
		if self.is_empty():
			self._tail = None
		return answer
	
	def enqueue(self, e):
		"""在尾节点加入一个元素"""
		newest = self._Node(e, None)
		if self.is_empty():
			self._head = newest
		else:
			self._tail._next = newest
			self._tail = newest
		self._size += 1
