from development.chapter6.ArrayQueue import Empty
from development.chapter7.PositionalList import PositionalList
from development.chapter9.PriorityQueueBase import PriorityQueueBase


class SortedPriorityQueue(PriorityQueueBase):
	'''基于为实现内部排序的优先级队列的有序优先级队列'''
	
	def __init__(self):
		'''创建一个空的列表'''
		self._data = PositionalList()
	
	def __len__(self):
		'''返回队列的长度'''
		return len(self._data)
	
	def add(self, key, value):
		'''添加一个key-value值在优先级队列中实现有序的插入'''
		newest = self._Item(key, value)
		walk = self._data.last()
		while walk is not None and newest < walk.element():
			walk = self._data.before(walk)
		if walk is None:
			self._data.add_first(newest)
		else:
			self._data.add_after(walk, newest)
	
	def min(self):
		'''返回优先级队列中的key值最下的一个'''
		if self.is_empty():
			raise Empty('队列为空')
		p = self._data.first()
		item = p.element()
		return (item._key, item._value)
	
	def remove_min(self):
		'''移出key值最小的元素并且返回key-value值'''
		if self.is_empty():
			raise Empty('队列为空')
		item = self._data.delete(self._data.first())
		return (item._key, item._value)

