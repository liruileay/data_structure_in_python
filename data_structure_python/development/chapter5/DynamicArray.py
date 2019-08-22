import ctypes


class DynamicArray(object):
	"""用一个动态的数组取实现python中的列表"""
	
	def __init__(self):
		"""创建一个空的数组"""
		self._n = 0                                 #记录数组中的元素个数
		self._capacity = 1                          #记录数组的最大容量
		self._A = self._make_array(self._capacity)
	
	def __len__(self):
		"""返回列表的长度"""
		return self._n
	
	def __getitem__(self, k):
		"""返回k索引对应的元素"""
		if not 0 <= k < self._n:
			raise IndexError("索引超出范围")
		return self._A[k]
	
	def append(self, obj):
		"""在列表的最后面添加一个元素"""
		if self._n == self._capacity:
			self._resize(2 * self._capacity)         # 对数组进行扩容
		self._A[self._n] = obj
		self._n += 1
	
	def _resize(self, c):
		"""原来数组进行扩容"""
		B = self._make_array(c)
		for k in range(self._n):
			B[k] = self._A[k]
		self._A = B
		self._capacity = c
	
	def _make_array(self, c):
		"""初始化一个能存储c个元素的数组"""
		return (c * ctypes.py_object)()              # 初始化一个指定长度的数组对象


array = DynamicArray()
for i in range(10):
	array.append(i)

print(len(array))
