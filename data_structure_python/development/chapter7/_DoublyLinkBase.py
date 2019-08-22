class _DoublyLinkedBase(object):
	"""双端链表基类"""
	
	class _Node:
		"""双向节点类"""
		__slots__ = '_element', '_next', '_prev'
		def __init__(self, element, prev, next):
			self._element = element
			self._prev = prev
			self._next = next
	
	def __init__(self):
		"""初始化一个双向链表其中头节点和尾节点都为空"""
		self._header = self._Node(None, None, None)
		self._trailer = self._Node(None, None, None)
		self._header._next = self._trailer
		self._trailer._prev = self._header
		self._size = 0
	
	def __len__(self):
		"""返回链表的长度"""
		return self._size
	
	def is_empty(self):
		return self._size == 0
	
	def _insert_between(self, e, predecessor, successor):
		"""创建一个新的节点插入两个节点中间"""
		newest = self._Node(e, predecessor, successor)
		predecessor._next = newest
		successor._prev = newest
		self._size += 1
		return newest
	
	def _delete_node(self, node):
		"""删除该节点并对父节点和子节点重新进行指向"""
		predecessor = node._prev
		successor = node._next
		predecessor._next = successor
		successor._prev = predecessor
		self._size -= 1
		element = node._element
		node._prev = node._next = node._element = None
		return element
