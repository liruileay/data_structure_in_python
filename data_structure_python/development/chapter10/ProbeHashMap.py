from development.chapter10.HashMapBase import HashMapBase


class ProbeHashMap(HashMapBase):
	'''用线性探测处理冲突'''
	_AVAIL = object()  # 表示一个哨兵用与删除后的标记
	
	def is_available(self, j):
		'''判断当前哈希表中是否有元素如果为None 或者为删除后的标记元素就表示这个j对应的哈希表的位置上面的位置是可用的返回True'''
		return self._table[j] is None or self._table[j] is ProbeHashMap._AVAIL
	
	def _find_slot(self, j, k):
		'''判断j位置对应的表的元素是否为空如果为空就返回False并且返回该位置的索引
			如果当前索引位置不为空就返回True和当前位置 或者寻找当前位置的k等于给定的k的位置返回True 和j的位置
		'''
		firstAvail = None
		while True:
			if self.is_available(j):
				if firstAvail is None:
					firstAvail = j
				if self._table[j] is None:
					return (False, firstAvail)
			elif self._table[j]._key == k:
				return (True, j)
			j = (j + 1) % len(self._table)
	
	def _bucket_getitem(self, j, k):
		'''获取j索引下的k值'''
		found, s = self._find_slot(j, k)
		if not found:
			raise KeyError('没有key对应的值')
		return self._table[s]._value
	
	def _bucket_setitem(self, j, k, v):
		'''给哈希表添加值'''
		found, s = self._find_slot(j, k)
		if not found:
			self._table[s] = self._Item(k, v)
			self._n += 1
		else:
			self._table[s]._value = v
	
	def _bucket_delitem(self, j, k):
		'''删除哈希表中的元素'''
		found, s = self._find_slot(j, k)
		if not found:
			raise KeyError('没有这样的k值')
		self._table[s] = ProbeHashMap._AVAIL
	
	def __iter__(self):
		'''将整个哈希表变成一个迭代器'''
		for j in range(len(self._table)):
			if not self.is_available(j):
				yield self._table[j]._key
