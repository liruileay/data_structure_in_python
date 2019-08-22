class MultiMap(object):
	'''集合多集合的映射实现'''
	
	_MapType = dict
	
	def __init__(self):
		'''创建一个空的集合的实例键对应的是key值对应的是一个列表'''
		self._map = self._MapType()
		self._n = 0
	
	def __iter__(self):
		'''将原来的变成一个可迭代的对象'''
		for k, secondary in self._map.items():
			for v in secondary:
				yield k, v
	
	def add(self, k, v):
		'''在原来的集合里面添加一个'''
		container = self._map.setdefault(k, [])
		container.append(v)
		self._n += 1
	
	def pop(self, k):
		'''从后面删除一个元素'''
		secondary = self._map[k]
		v = secondary.pop()
		if len(secondary) == 0:
			del self._map[k]
		self._n -= 1
		return (k, v)
	
	def find(self, k):
		'''找到key为k的元素返回'''
		seconday = self._map[k]
		return (k, seconday[0])
	
	def find_all(self, k):
		'''找到所有值为k的元素'''
		secondary = self._map.get(k, [])
		for v in secondary:
			yield (k, v)
