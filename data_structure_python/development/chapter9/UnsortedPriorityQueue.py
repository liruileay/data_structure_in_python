from development.chapter6.ArrayQueue import Empty
from development.chapter7.PositionalList import PositionalList
from development.chapter9.PriorityQueueBase import PriorityQueueBase


class UnsortedPriorityQueue(PriorityQueueBase):
	'''实现一个内部没有排序的优先级队列的表'''
	
	def _find_min(self):
		'''返回这个key值最小的_Item节点对应的emement'''
		if self.is_empty():
			raise Empty('节点不能为空')
		small = self._data.first()
		walker = self._data.after(small)
		while walker is not None:
			if walker.element() < small.element():
				small = walker
			walker = self._data.after(walker)
		return small
	
	def __init__(self):
		'''创建一个新的空的队列'''
		self._data = PositionalList()
	
	def __len__(self):
		'''返回队列的长度'''
		return len(self._data)
	
	def add(self, key, value):
		'''给优先级队列中添加一个元素'''
		self._data.add_last(self._Item(key, value))
	
	def min(self):
		'''返回但是不移出key值最小的元素'''
		p = self._find_min()
		item = p.element()
		return (item._key, item._value)
	
	def remove_min(self):
		'''移出最小的key对应的节点并且返回节点的key和value'''
		p = self._find_min()
		item = self._data.delete(p)
		return (item._key, item._value)
