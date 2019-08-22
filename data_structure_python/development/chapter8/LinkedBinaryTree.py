from development.chapter8.BinaryTree import BinaryTree


class LinkedBinaryTree(BinaryTree):
	'''链式二叉树的python实现'''
	
	class _Node:
		__slots__ = '_element', '_parent', '_left', '_right'
		
		def __init__(self, element, parent=None, left=None, right=None):
			'''初始化一个树节点包含树的元素父节点左孩子右孩子'''
			self._element = element
			self._parent = parent
			self._left = left
			self._right = right
	
	class Position(BinaryTree.Position):
		'''将抽象的位置类进行重写'''
		
		def __init__(self, container, node):
			self._container = container
			self._node = node
		
		def element(self):
			'''返回树节点的元素值'''
			return self._node._element
		
		def __eq__(self, other):
			'''返回true如果其他的节点和该节点的位置相同'''
			return type(other) is type(self) and other._node is self._node
	
	def _vaildate(self, p):
		'''校验该节点的位置看是否满足要求'''
		if not isinstance(p, self.Position):
			raise TypeError('必须是位置类Position的一个实例')
		if p._container is not self:
			raise TypeError('p的所有类不是LinkedBinaryTree')
		if p._node._parent is p._node:
			raise ValueError('p不再有效父节点是自己没有意义')
		return p._node
	
	def _make_position(self, node):
		'''确定该节点的位置并且返回node'''
		return self.Position(self, node)._node if node is not None else None
	
	def __init__(self):
		'''初始化创建一个空的二叉树'''
		self._root = None
		self._size = 0
	
	def __len__(self):
		'''返回树的节点个数'''
		return self._size
	
	def root(self):
		'''返回该树的根节点的位置'''
		return self._make_position(self._root)
	
	def parent(self, p):
		'''返回该位置的父类'''
		node = self._vaildate(p)
		return self._make_position(node._parent)
	
	def left(self, p):
		'''返回该位置的左孩子的位置'''
		node = self._vaildate(p)
		return self._make_position(node._left)
	
	def right(self, p):
		'''返回该位置的孩子的位置'''
		node = self._vaildate(p)
		return self._make_position(node._right)
	
	def num_children(self, p):
		'''返回该节点的孩子节点的数量'''
		node = self._vaildate(p)
		count = 0
		if node._left is not None:
			count += 1
		if node._right is not None:
			count += 1
		return count
	
	def _add_root(self, e):
		'''为树添加一个根节点'''
		if self.root() is not None:raise ValueError('头节点不为空不能添加')
		self._root = self._Node(e)
		self._size =1
		return self.Position(self,self._root)
	
	def _add_left(self, p, e):
		'''给该节点添加左孩子'''
		node = self._vaildate(p)
		if node._left is not None: raise ValueError('该树的左孩子存在')
		self._size += 1
		node._left = self._Node(e,node)
		return self._make_position(node._left)
	
	def _add_right(self, p, e):
		'''给该节点添加右孩子'''
		node = self._vaildate(p)
		if node._left is not None: raise ValueError('左孩子部位空无法添加')
		node._right = self._Node(e,node)
		return self._make_position(node._right)
		
	def _replace(self, p, e):
		'''替换该节点的位置的元素'''
		node = self._vaildate(p)
		old = node._element()
		node._element = e
		return old
	
	def _delete(self, p):
		'''删除该位置的节点并且用它的孩子替换'''
		node = self._vaildate(p)
		if node.num_children(p) ==2:raise ValueError('p有两个孩子无法删除')
		child = node._left if node._left else node._right
		if child is not None:
			child._parent = node._parent
		if node is self._root:
			self._root = child
		else:
			parent = node._parent
			if node is parent._left:
				parent._left = child
			if node is parent._right:
				parent._right = child
		self._size +=1
		node._parent = node
		return node._element
	
	def _attach(self, p, t1, t2):
		'''将t1和t2连接成p的左子树和右子树'''
		node = self._vaildate(p)
		if not self.is_leaf(p):raise ValueError('位置必须是页节点')
		if not type(self) is type(t1) is type(t2):
			raise TypeError('必须是同一种内型的才可以连接')
		self._size +=len(t1) + len(t2)
		if not t1.is_empty:
			t1._root._parent = node
			node._left = t1._root
			t1._root = None
			t1._size = 0
		if not t2.is_empty:
			t2._root._parent = node
			node._left =t2._root
			t2.root = None
			t2._size = 0