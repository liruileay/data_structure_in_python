from development.chapter6.ArrayQueue import Empty


class Stack(object):
	"""设计一个基于列表的栈这个栈具有getMin功能"""
	
	def __init__(self):
		self._data = []
		self._help = []
	
	def __len__(self):
		"""获取栈中元素的个数"""
		return len(self._data)
	
	def is_empty(self):
		"""判断栈中元素是否为空"""
		return len(self._data) == 0
	
	def push(self, v):
		if self.is_empty():
			self._data.append(v)
			self._help.append(v)
		else:
			self._data.append(v)
			max = self._help.pop()
			if max >= v:
				self._help.append(max)
				self._help.append(v)
			else:
				self._help.append(max)
				self._help.append(max)
	
	def pop(self):
		"""弹出最后一个进栈的元素"""
		if self.is_empty():
			raise Empty("Stack is empty")
		self._help.pop()
		return self._data.pop()
	
	def get_min(self):
		"""弹出栈中最小的元素"""
		if self.is_empty():
			raise Empty("Stack is empty")
		self._data.pop()
		return self._help.pop()


if __name__ == '__main__':
	s = Stack()
	for i in [3, 34, 5, 45, 45, 45, 6, 7, 7, 7, 7435, 345, 1, 3]:
		s.push(i)
	for i in range(8):
		print(s.get_min())
