from development.chapter6.ArrayQueue import Empty

class ArrayStack(object):
	"""每次从栈顶弹出一个"""
	class _Node:
		__slots__ = '_element', '_next'
		
		def __init__(self, element, next):
			'''节点类记录一个元素和该节点的下一个节点'''
			self._element = element
			self._next = next
	
	def __init__(self):
		'''初始化记录栈的大小和栈顶'''
		self._size = 0
		self._head = None
	
	def is_empty(self):
		'''判断该栈是否为空'''
		return self._size == 0
	
	def __len__(self):
		'''返回栈的长度'''
		return self._size
	
	def push(self, e):
		'''在栈顶添加一个元素'''
		self._head = self._Node(e, self._head)
		self._size += 1
	
	def top(self):
		'''查看栈顶元素'''
		if self.is_empty():
			raise Empty("Stack is empty")
		return self._head._element()
	
	def pop(self):
		'''删除栈顶的元素'''
		if self.is_empty():
			raise Empty("Stack is empty")
		answer = self._head._element
		self._head = self._head._next
		self._size -= 1
		return answer
