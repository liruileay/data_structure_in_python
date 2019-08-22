from development.chapter9.HeapPriorityQueue import HeapPriorityQueue


class AdaptableHeapPriorityQueue(HeapPriorityQueue):
	'''一个可适应性优先级队列的实现'''
	
	class Locator(HeapPriorityQueue._Item):
		__slots__ = '_index'
		
		def __init__(self, k, v, j):
			'''多了一个描述原来位置的元素j'''
			super().__init__(k, v)
			self._index = j
	
	def _swap(self, i, j):
		'''交换两个元素的值并且他们的index也要交换'''
		super()._swap(i, j)
		self._data[i]._index = i
		self._data[j]._index = j
	
	def _bubble(self, j):
		'''根据给定的位置判断是向上冒泡还是向下冒泡'''
		if j > 0 and self._data[j] < self._data[self._parent(j)]:
			self._unheap(j)
		else:
			self._downheap(j)
	
	def add(self, key, value):
		'''添加一个key-value返回一个loc对象'''
		token = self.Locator(key, value, len(self._data))
		self._data.append(token)
		self._unheap(len(self._data) - 1)
		return token
	
	def update(self, loc, newkey, newval):
		'''更新指定索引位置的key-value'''
		j = loc._index
		if not (0 <= j < len(self) and self._data[j] is loc):
			raise ValueError('loc 错误')
		loc._key = newkey
		loc._value = newval
		self._bubble(j)
	
	def remove(self, loc):
		'''删除指定位置的元素'''
		j = loc._index
		if not (0 <= j < len(self) and self._data[j] is loc):
			raise ValueError('loc 值错误')
		if j == len(self) - 1:
			self._data.pop()
		else:
			self._swap(j, len(self) - 1)
			self._bubble(j)
		return (loc._key, loc._value)
