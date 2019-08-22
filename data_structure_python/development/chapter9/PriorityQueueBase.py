class PriorityQueueBase(object):
	'''一个抽象的优先级队列的基类'''
	
	class _Item:
		'''记录优先级队列的节点的值和k'''
		__slots__ = '_key', '_value'
		
		def __init__(self, key, value):
			self._key = key
			self._value = value
		
		def __lt__(self, other):
			return self._key < other._key
	
	def is_empty(self):
		'''判断队列是否为空'''
		return len(self) == 0
