class Empty(Exception):
	pass


class ArrayQueue(object):
	"""用长度动态变化的数组实现一个队列"""
	DEFAULT_CAPACITY = 10
	
	def __init__(self):
		"""初始化数组的长度最大容纳元素个数和队列的头节点位置"""
		self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
		self._size = 0
		self._front = 0
	
	def __len__(self):
		return self._size
	
	def is_empty(self):
		return self._size == 0
	
	def first(self):
		"""查看d队列中第一个进入的元素"""
		if self.is_empty():
			raise Empty("Queue is empty")
		return self._data[self._front]
	
	def dequeue(self):
		"""元素进入队列"""
		if self.is_empty():
			raise Empty("Queue is empty")
		answer = self._data[self._front]
		self._data[self._front] = None
		self._front = (self._front + 1) % len(self._data)
		return answer
	
	def enqueue(self, value):
		"""元素出队列"""
		if self._size == len(self._data):
			self._resize(2 * self._size)
		avail = (self._front + self._size) % len(self._data)
		self._data[avail] = value
		self._size += 1
	
		
	def _resize(self, cap):
		"""对数组进行扩容"""
		old = self._data
		self._data = [None] * cap
		walk = self._front
		for k in range(self._size):
			self._data[k] = old[walk]
			walk = (1 + walk) % len(old)
		self._front = 0
