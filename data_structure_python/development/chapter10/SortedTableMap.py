from development.chapter10.MapBase import MapBase


class SortedTableMap(MapBase):
	'''排序检索表表中的元素按照key值进行排序'''
	
	def _find_index(self, k, low, high):
		'''在索引为low--->high里面找到k值对应的表中的位置j返回'''
		if high < low:
			return high + 1  # 如果是添加不存在就将在列表后面添加一个索引个新的元素存储
		else:
			mid = (high + low) // 2
			if k == self._table[mid]._key:
				return mid
			elif k < self._table[mid]._key:
				return self._find_index(k, low, mid - 1)
			return self._find_index(k, mid + 1, high)
	
	def __init__(self):
		'''初始化一个空数组'''
		self._table = []
	
	def __len__(self):
		'''返回表的长度'''
		return len(self._table)
	
	def __getitem__(self, k):
		'''获取k对应的value值如果不存在这给就报错'''
		j = self._find_index(k, 0, len(self._table) - 1)
		if j == len(self._table) or self._table[j]._key != k:
			raise KeyError('k索引不存在')
		return self._table[j]._value
	
	def __setitem__(self, k, v):
		'''重新设置k对应的value值维v'''
		j = self._find_index(k, 0, len(self._table) - 1)
		if j < len(self._table) and self._table[j]._key == k:
			self._table[j]._value = v
		else:
			self._table.insert(j, self._Item(k, v))
	
	def __delitem__(self, k):
		'''删除key=k出的item'''
		j = self._find_index(k, 0, len(self._table) - 1)
		if j == len(self._table) or self._table[j]._key != k:
			raise KeyError('k索引不存在')
		self._table.pop(j)
	
	def __iter__(self):
		'''将表生成一个迭代器'''
		for item in self._table:
			yield item._key
	
	def _reversed__(self):
		'''生成一个反序的迭代器'''
		for item in reversed(self._table):
			yield item._key
	
	def find_min(self):
		'''返回索引k最小的key对应的key-value　　排序后的第一个'''
		if len(self._table) > 0:
			return (self._table[0]._key, self._table[0]._value)
		return None
	
	def find_max(self):
		'''返回索引k最大的key对应的key-value　　排序后的最后一个'''
		if len(self._table) > 0:
			return (self._table[-1]._key, self._table[-1]._value)
		return None
	
	def find_ge(self, k):
		'''返回k大于或者等于k的全部值'''
		j = self._find_index(k, 0, len(self._table) - 1)
		if j < len(self._table):
			return (self._table[j]._key, self._table[j]._value)
		return None
	
	def find_lt(self, k):
		'''查找小于k的'''
		j = self._find_index(k, 0, len(self._table) - 1)
		if j > 0:
			return (self._table[j - 1]._key, self._table[j - 1]._value)
		return None
	
	def find_gt(self, k):
		'''查找大于k的'''
		j = self._find_index(k, 0, len(self._table) - 1)
		if j < len(self._table) and self._table[j]._key == k:
			j += 1
		if j < len(self._table):
			return (self._table[j]._key, self._table[j]._value)
		return None
	
	def find_le(self, k):
		'''返回k小于或者等于k的全部值'''
		j = self._find_index(k, 0, len(self._table) - 1)
		if j < len(self._table):
			return (self._table[j]._key, self._table[j]._value)
		return None
	
	def find_range(self, start, stop):
		'''查找key值在start到stop范围的'''
		if start is None:
			return 0
		else:
			j = self._find_index(start, 0, len(self._table) - 1)
			while j < len(self._table) and (stop is None or self._table[j]._key < stop):
				yield (self._table[j]._key, self._table[j]._value)
				j += 1
