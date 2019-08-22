from development.chapter10.MapBase import MapBase


class UnsortedTableMap(MapBase):
	'''使用无序列表映射实现'''
	
	def __init__(self):
		'''创建一个空的列表'''
		self._table = []
	
	def __getitem__(self, k):
		'''返回k对应的键值如果没有找到就报错'''
		for item in self._table:
			if item._key == k:
				return item._value
		raise KeyError('不存在这样的key值')
	
	def __setitem__(self, k, v):
		'''给列表设置值'''
		for item in self._table:
			if item._key == k:
				item._value = v
		self._table.append(self._Item(k, v))
	
	def __delitem__(self, k):
		'''删除key对应的值如果不存在就报错'''
		for j in range(len(self._table)):
			if self._table[j]._key == k:
				self._table.pop(j)
		raise KeyError('不存在这样的key值')
	
	def __len__(self):
		'''列表的长度'''
		return len(self._table)
	
	def __iter__(self):
		'''返回所有的key值的一个迭代'''
		for item in self._table:
			yield item._key
