from development.chapter6.ArrayQueue import Empty
from development.chapter9.PriorityQueueBase import PriorityQueueBase


class HeapPriorityQueue(PriorityQueueBase):
	'''基于数组的堆实现优先级队列'''
	
	def _parent(self, j):
		'''找到父节点对应的索引'''
		return (j - 1) // 2
	
	def _left(self, j):
		'''找到左孩子对应的索引'''
		return 2 * j + 1
	
	def _right(self, j):
		'''找到右几点的孩子'''
		return 2 * j + 2
	
	def _has_left(self, j):
		'''判断是否右左孩子'''
		return self._left(j) < len(self._data)
	
	def _has_right(self, j):
		'''判断是否有右孩子'''
		return self._right(j) < len(self._data)
	
	def _swap(self, i, j):
		'''交换两个索引对应元素的值'''
		self._data[i], self._data[j] = self._data[j], self._data[i]
	
	def _unheap(self, j):
		'''如果一个节点的子节点小于就和子节点交换   ->向上冒泡'''
		parent = self._parent(j)
		if j > 0 and self._data[j] < self._data[parent]:
			self._swap(j, parent)
			self._unheap(parent)
	
	def _downheap(self, j):
		'''开左右孩子中最小的那个是不是比自己小比自己小就向下冒泡'''
		if self._has_right(j):
			left = self._left(j)
			small_child = left
			if self._has_right(j):
				right = self._right(j)
				if self._data[right] < self._data[left]:
					small_child = right
			if self._data[small_child] < self._data[j]:
				self._swap(j, small_child)
				self._downheap(small_child)
		
	def __init__(self):
		'''创建一个空的数组'''
		self._data = []
	
	def __len__(self):
		'''返回数组的长度'''
		return len(self._data)
	
	def add(self, key, value):
		'''给这个数组添加一个key-value'''
		self._data.append(self._Item(key, value))
		self._unheap(len(self._data) - 1)
	
	def min(self):
		'''返回这个数组中key最小的一个但是不删除这个节点'''
		if self.is_empty():
			raise Empty('队列元素为空')
		item = self._data[0]
		return (item._key, item._value)
	
	def remove_min(self):
		'''删除key值最小的那个元素并且返回元素的key-value'''
		if self.is_empty():
			raise Empty('队列元素为空')
		self._swap(0, len(self._data) - 1)
		item = self._data.pop()
		self._downheap(0)
		return (item._key, item._value)

