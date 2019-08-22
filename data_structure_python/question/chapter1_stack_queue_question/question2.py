from development.chapter6.ArrayStack import ArrayStack, Empty


class Queue(object):
	"""用两个栈实现一个队列,实现队列的性质"""
	
	def __init__(self):
		"""创建两个栈来支持队列的操作"""
		self._data = ArrayStack()
		self._help = ArrayStack()
	
	def push(self, v):
		"""向数组中添加一个元素"""
		self._data.push(v)
	
	def pop(self):
		"""删除第一个进入的元素"""
		if self._data.is_empty():
			raise Empty("Queue is empty")
		while not self._data.is_empty():
			self._help.push(self._data.pop())
		value = self._help.pop()
		while not self._help.is_empty():
			self._data.push(self._help.pop())
		return value
	
	def top(self):
		"""查看队列的第一个元素"""
		if self._data.is_empty():
			raise Empty("Queue is empty")
		while not self._data.is_empty():
			self._help.push(self._data.pop())
		value = self._help.top()
		while not self._help.is_empty():
			self._data.push(self._help.pop())
		return value


if __name__ == '__main__':
	q = Queue()
	for i in [1, 5, 4, 54, 56, 5, 4]:
		q.push(i)
	print("第一元素是{}".format(q.top()))
	for i in range(7):
		print(q.pop())
