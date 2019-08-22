from development.chapter6.ArrayQueue import Empty


class DoubleArrayQueue(object):
	"""用动态数组实现一个双向队列"""
	DEFAULT_CAPACITY = 10
	
	def __init__(self):
		"""初始化动态数组的长度"""
		self._data = [None] * DoubleArrayQueue.DEFAULT_CAPACITY
		self._front = 0
		self._size = 0
	
	def add_last(self, value):
		"""从数组的最后面添加一个元素"""
		if self._size == len(self._data):
			self._resize(2 * len(self._data))
		avail = (self._front + self._size) % len(self._data)
		self._data[avail] = value
		self._size += 1
	
	def add_first(self, value):
		"""丛数组的顶部添加一个元素"""
		if self._size == len(self._data):
			self._resize(2 * len(self._data))
		self._front = (self._front - 1) % len(self._front)
		self._data[self._front] = value
		self._size += 1
	
	def delete_first(self):
		"""删除数组的第一个元素"""
		if self.is_empty():
			raise Empty("Queue is empty")
		answer = self._data[self._front]
		self._data[self._front] = None
		self._front = (self._front + 1) % len(self._data)
		self._size -= 1
		return answer
	
	def delete_last(self):
		"""删除数组的最后一个元素"""
		if self.is_empty():
			raise Empty("Queue is empty")
		end_index = (self._front + self._size - 1) % len(self._data)
		answer = self._data[end_index]
		self._data[end_index] = None
		self._size -= 1
		return answer
	
	def is_empty(self):
		"""判断数组是不是为空"""
		return self._size == 0
	
	def last(self):
		"""查看数组的最后一个元素"""
		if self.is_empty():
			raise Empty("Queue is empty")
		return self._data[(self._front + self._size - 1) % len(self._data)]
	
	def first(self):
		"""产看数组的第一个元素"""
		if self.is_empty():
			raise Empty("Queue is empty")
		return self._data[self._front]
	
	def _resize(self, cap):
		"""对数组进行扩容"""
		old = self._data
		self._data = [None] * cap
		walk = self._front
		for k in range(len(old)):
			self._data[k] = old[walk]
			walk = (self._front + 1) % len(old)
		self._front = 0
