from development.chapter10.SortedTableMap import SortedTableMap


class CostPerformanceDatabase:
	'''使用有序映射维持最大值集'''
	
	def __init__(self):
		'''创建一个空的数据库表'''
		self._M = SortedTableMap()
	
	def best(self, k):
		'''返回价格为c的最好的价格性能对，如果没有及返回None'''
		return self._M.find_le(k)
	
	def add(self, k, p):
		'''添加一个花费为c性能为p的'''
		other = self._M.find_le(k)
		if other is not None and other[1] >= p:
			return
		self._M[k] = p
		other = self._M.find_gt(k)
		# 删除后面性能比他小的
		while other is not None and other[1] <= p:
			del self._M[other[0]]
			other = self._M.find_gt(k)
