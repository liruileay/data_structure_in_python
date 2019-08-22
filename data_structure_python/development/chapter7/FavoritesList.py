from development.chapter7.PositionalList import PositionalList


class FavoritesList(object):
	class _Item:
		"""记录节点的元素和节点元素被访问的次数"""
		__slots__ = '_value', '_count'
		
		def __init__(self, e):
			self._value = e
			self._count = 0
	
	def __init__(self):
		self._data = PositionalList()
	
	def __len__(self):
		return len(self._data)
	
	def _find_position(self, e):
		"""查询看列表中有没有元素值位e的节点"""
		walk = self._data.first()
		while walk is not None and walk.element()._value != e:
			walk = self._data.after(walk)
		return walk
	
	def _move_up(self, p):
		"""对列表按照访问的次数从大到小排序"""
		if p != self._data.first():
			cnt = p.element()._count
			walk = self._data.before(p)
			if walk.element()._count < cnt:
				while walk != self._data.first() and self._data.before(walk).element()._count < cnt:
					walk = self._data.before(walk)
				self._data.add_before(walk, self._data.delete(p))
	
	def is_empty(self):
		"""判断列表是否为空"""
		return self._data.is_empty()
	
	def access(self, e):
		"""通过比对元素统计访问量没有该元素就创建"""
		p = self._find_position(e)
		if p is None:
			p = self._data.add_last(self._Item(e))
		p.element()._count += 1
		self._move_up(p)
	
	def remove(self, e):
		"""删除指定元素对应的节点"""
		p = self._find_position(e)
		if p is not None:
			self._data.delete(p)
	
	def top(self, k):
		"""返回前访问量排在前k个的节点元素"""
		if not 1 <= k <= len(self._data):
			raise ValueError("最多只有{}个元素".format(len(self._data)))
		walk = self._data.first()
		for k in range(k):
			yield walk.element()._value
			walk = self._data.after(walk)
	
	def __repr__(self):
		"""打印出整个结构"""
		return ','.join('({0}:{1})'.format(i._value, i._count) for i in self._data)


if __name__ == '__main__':
	fav = FavoritesList()
	for c in 'hello. this is a test of mtf':  # well, not the mtf part...
		fav.access(c)
	print(fav)