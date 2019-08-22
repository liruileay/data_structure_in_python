from random import randrange

from development.chapter10.MapBase import MapBase


class HashMapBase(MapBase):
	'''一个哈希表示实现的抽象基类'''
	
	def __init__(self, cap=11, p=109345121):
		'''创建一个空的哈希表'''
		self._table = cap * [None]
		self._n = 0  # 表示哈希表中key_value的个数
		self._prime = p
		self._scale = 1 + randrange(p - 1)
		self._shift = randrange(p)
	
	def _hash_function(self, k):
		'''将k进行hash返回一个hash值该哈希值表示了元素应该在那个桶'''
		return (hash(k) * self._scale + self._shift) % self._prime % len(self._table)
	
	def __getitem__(self, k):
		'''从哈希表中获取值'''
		j = self._hash_function(k)
		return self._bucket_getitem(j, k)
	
	def __setitem__(self, k, v):
		'''设置值到哈希表中'''
		j = self._hash_function(k)
		self._bucket_setitem(j, k, v)
		if self._n > len(self._table) // 2:  # 保持负载因子<= 0.5
			self._resize(2 * len(self._table) - 1)
	
	def __delitem__(self, k):
		'''从哈希表中删除'''
		j = self._hash_function(k)
		self._bucket_delitem(j, k)
		self._n -= 1
	
	def __len__(self):
		'''返回哈希表的长度'''
		return self._n
	
	def _resize(self, c):
		'''对原来的数组进行扩容'''
		old = list(self.items())
		self._table = c * [None]
		self._n = 0
		for k, v in old:
			self._table[k] = v
