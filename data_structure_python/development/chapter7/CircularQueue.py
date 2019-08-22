from development.chapter6.ArrayQueue import Empty


class CircularQueue(object):
	"""循环链表实现一个队列"""
	
	class _Node:
		__slots__ = '_element', '_next'
		
		def __init__(self, element, next):
			'''记录节点元素和该节点的下一个节点'''
			self._next = next
			self._element = element
	
	def __init__(self):
		"""初始化节点的尾部哨兵节点和链表的长度"""
		self._tail = None
		self._size = 0
	
	def __len__(self):
		'''返回该队列的长度'''
		return self._size
	
	def is_empty(self):
		'''判读该队列是否为空'''
		return self._size == 0
	
	def first(self):
		"""返回循环链表头节点的元素"""
		if self.is_empty():
			raise Empty("Queue is empty")
		return self._tail._next._element
	
	def dequeue(self):
		"""删除一个节点"""
		if self.is_empty():
			raise Empty("Queue is empty")
		oldest = self._tail._element
		if self._size == 1:
			self._tail = None
		else:
			self._tail._next = oldest._next
		self._size -= 1
		return oldest._element
	
	def enqueue(self, e):
		"""创建并且添加一个节点"""
		newest = self._Node(e, None)
		if self.is_empty():
			newest._next = newest
		else:
			newest._next = self._tail._next
			self._tail._next = newest
		self._tail = newest
		self._size += 1
	
	def rotate(self):
		'''移动哨兵节点的位置'''
		if self._size > 0:
			self._tail = self._tail._next
