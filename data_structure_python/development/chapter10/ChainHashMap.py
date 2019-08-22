from development.chapter10.HashMapBase import HashMapBase
from development.chapter10.UnsortedTableMap import UnsortedTableMap


class ChainHashMap(HashMapBase):
	'''用分离链表实现的具体哈希map类'''
	
	def _bucket_getitem(self, j, k):
		'''获取到列表中对应的同种的值'''
		bucket = self._table[j]
		if bucket is None:
			raise KeyError('没有这样的key值')
		return bucket[k]
	
	def _bucket_setitem(self, j, k, v):
		'''设置到列表中的一个桶一个值'''
		if self._table[j] is None:
			self._table[j] = UnsortedTableMap()
		oldsize = len(self._table[j])
		self._table[j][k] = v
		if len(self._table[j]) > oldsize:
			self._n += 1
	
	def _bucket_delitem(self, j, k):
		'''删除列表中对应j桶的k对应的键值对'''
		bucket = self._table[j]
		if bucket is None:
			raise KeyError('不存在样的k值')
		del bucket[k]

	
	def __iter__(self):
		'''迭代出所有的元素值'''
		for bucket in self._table:
			if bucket is not None:
				for key in bucket:
					yield key

