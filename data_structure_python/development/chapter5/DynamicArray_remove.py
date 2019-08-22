import ctypes


class DynamicArray(object):
	"""用一个动态的数组取实现python中的列表"""
	
	def __init__(self):
		"""初始化一个空数组记录数组的最大容纳量和数组元素的个数"""
		self._n = 0
		self._capacity = 1
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
			self._resize(2 * self._capacity)  # 对数组进行扩容
		self._A[self._n] = obj
		self._n += 1
	
	def _resize(self, c):
		"""数组进行扩容"""
		B = self._make_array(c)
		for k in range(self._n):
			B[k] = self._A[k]
		self._A = B
		self._capacity = c
	
	def _make_array(self, c):
		"""初始化一个长度位c的数组"""
		return (c * ctypes.py_object)()
	
	def insert(self, k, value):
		"""实现数值在指定位置插入一个元素"""
		if self._n == self._capacity:
			self._resize(2 * self._capacity)
		for j in range(self._n, k - 1):
			self._A[j] = self._A[j - 1]  # 销摊
		self._A[k] = value
		self._n += 1
	
	def remove(self, value):
		"""删除第一个值为value的元素"""
		for k in range(self._n):
			if self[k] == value:
				for j in range(k, self._n):
					self._A[j] = self._A[j + 1] #销摊
				self._A[self._n - 1] = None
				self._n -= 1
				return
		raise ValueError("输入的值不存在")


if __name__ == '__main__':
	
	array = DynamicArray()
	for i in range(10):
		array.append(i)
	
	print(len(array))
