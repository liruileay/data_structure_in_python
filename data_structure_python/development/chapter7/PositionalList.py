from development.chapter7._DoublyLinkBase import _DoublyLinkedBase


class PositionalList(_DoublyLinkedBase):
	"""利用双向链表实现一个列表"""
	
	class Position:
		"""记录节点的位置"""
		
		def __init__(self, container, node):
			'''记录该类是在PositionalList里面和节点'''
			self._container = container
			self._node = node
		
		def element(self):
			'''返回该位置节点的元素'''
			return self._node._element
		
		def __eq__(self, other):
			return type(other) is type(self) and other._node is self._node
		
		def __ne__(self, other):
			return not (self == other)
	
	def _vaildate(self, p):
		"""对传入过来的p对象进行验证"""
		if not isinstance(p, self.Position):
			raise TabError("p mast be proper Position type")
		if p._container is not self:
			raise ValueError("p does not belong to this container")
		if p._node._next is None:
			raise ValueError("p is no longer vaild")
		return p._node
	
	def _make_position(self, node):
		"""确定传入节点的位置返回p对象"""
		if node is self._header or node is self._trailer:
			return None
		return self.Position(self, node)
	
	def _insert_between(self, e, predecessor, successor):
		"""将节点插入只当的位置并且返回插入节点的位置"""
		node = super()._insert_between(e, predecessor, successor)
		return self._make_position(node)
	
	def first(self):
		"""返回第一个节点的位置"""
		return self._make_position(self._header._next)
	
	def last(self):
		"""返回最后一个节点的位置"""
		return self._make_position(self._trailer._prev)
	
	def before(self, p):
		"""得到p的前一个节点的位置"""
		node = self._vaildate(p)
		return self._make_position(node._prev)
	
	def after(self, p):
		"""得到p节点后一个的位置"""
		node = self._vaildate(p)
		return self._make_position(node._next)
	
	def __iter__(self):
		"""迭代器实现返回对象中的元素"""
		cursor = self.first()
		while cursor is not None:
			yield cursor.element()
			cursor = self.after(cursor)
	
	def add_first(self, e):
		"""在头节点添加返回p对象"""
		return self._insert_between(e, self._header, self._header._next)
	
	def add_last(self, e):
		"""在尾节点添加返回p对象"""
		return self._insert_between(e, self._trailer._prev, self._trailer)
	
	def add_before(self, p, e):
		"""在p节点的前面添加一个节点返回p对象"""
		original = self._vaildate(p)
		return self._insert_between(e, original._prev, original)
	
	def add_after(self, p, e):
		"""在p节点的后面添加一个节点返回p对象"""
		original = self._vaildate(p)
		return self._insert_between(e, original, original._next)
	
	def delete(self, p):
		"""删除p节点"""
		original = self._vaildate(p)
		return self._delete_node(original)
	
	def replace(self, p, e):
		"""将p节点中的原属用e来代替"""
		original = self._vaildate(p)
		old_value = original._element
		original._element = e
		return old_value



if __name__ == '__main__':
	list = PositionalList()
	for i in range(100):
		list.add_first(i)
		list.add_last(2 * i)
	for k in list:
		print(k)
