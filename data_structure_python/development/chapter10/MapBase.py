from collections import MutableMapping


class MapBase(MutableMapping):
	'''一个抽象的基类满足各种映射应用'''
	
	class _Item:
		__slots__ = '_key', '_value'
		
		def __init__(self, k, v):
			'''key表示权重v表示值的大小'''
			self._key = k
			self._value = v
		
		def __eq__(self, other):
			'''定义相等的属性'''
			return self._key == other._key
		
		def __ne__(self, other):
			'''判断两个连个值是不相等的'''
			return not (self == other)
	
		def __lt__(self, other):
			'''等一等于的行为'''
			return self._key < other._key
	