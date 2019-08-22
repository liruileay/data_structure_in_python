from development.chapter9.PriorityQueueBase import PriorityQueueBase


class HeapifyFromDown(PriorityQueueBase):
	
	def __init__(self, contents):
		self._data = [self._Item(key, value) for key, value in contents]
		if len(self._data):
			self._heapify()
	
	def _heapify(self):
		'''自下而上的构建堆'''
		start = self._parent(len(self._data) - 1)
		for j in range(start, -1, -1):
			self._downheap(j)
	
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
