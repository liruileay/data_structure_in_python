from development.chapter11.TreeMap import TreeMap


class RedBlackTreeMap(TreeMap):
	'''基于脸熟二叉树的红黑树的实现'''
	
	class _Node(TreeMap._Node):
		'''给节点添加一个红节点属性'''
		__slots__ = '_red'
		
		def __init__(self, element, parent=None, left=None, right=None):
			'''给树添加一个红的属性'''
			super().__init__(element, parent, left, right)
			self._red = True
	
	def _set_red(self, p):
		'''设置节点p的颜色为红色'''
		p._node._red = True
	
	def _set_black(self, p):
		'''设置节点p的颜色为黑色'''
		p._node._red = False
	
	def _set_color(self, p, make_red):
		'''给节点设置指定的颜色'''
		p._node._red = make_red
	
	def _is_red(self, p):
		'''判断节点的颜色'''
		return p is not None and p._node._red
	
	def _is_red_leaf(self, p):
		'''判断节点p是不是叶节点并且是不是红色的'''
		return self._is_red(p) and self.is_leaf(p)
	
	def _get_red_child(self, p):
		'''返回一个红色的孩子节点如果没有就返回None'''
		for child in (self.left(p), self.right(p)):
			if self._is_red(child):
				return child
		return None
	
	def _resolve_red(self, p):
		'''构建一颗红黑树'''
		if self.is_root(p):
			self._set_black(p)
		else:
			parent = self.parent(p)
			if self._is_red(parent):
				uncle = self.sibling(parent)
				if not self._is_red(uncle):
					middle = self._restructure(p)
					self._set_black(middle)
					self._set_red(self.left(middle))
					self._set_red(self.right(middle))
				else:
					grand = self.parent(parent)
					self._set_red(grand)
					self._set_black(self.left(grand))
					self._set_black(self.right(grand))
					self._resolve_red(grand)
	
	def _rebalance_delete(self, p):
		'''删除后对一个红黑树进行重构'''
		if len(self) == 1:
			self._set_black(self.root())
		elif p is not None:
			n = self.num_children(p)
			if n == 1:
				c = next(self.children(p))
				if not self._is_red_leaf(c):
					self._fix_deficit(p, c)
			elif n == 2:
				if self._is_red_leaf(self.left(p)):
					self._set_black(self.left(p))
				else:
					self._set_black(self.right(p))
	
	def _fix_deficit(self, z, y):
		'''重新设置红黑树使其满足(2,4)树的属性的红黑树'''
		if not self._is_red(y):
			x = self._get_red_child(y)
			if x is not None:
				old_color = self._is_red(z)
				middle = self._restructure(x)
				self._set_color(middle, old_color)
				self._set_black(self.left(middle))
				self._set_black(self.right(middle))
			else:
				self._set_red(y)
				if self._is_red(z):
					self._set_black(z)
				elif not self.is_root(z):
					self._fix_deficit(self.parent(z), self.sibling(z))
		else:
			self._rotate(y)
			self._set_black(y)
			self._set_red(z)
			if z == self.right(y):
				self._fix_deficit(z, self.left(z))
			else:
				self._fix_deficit(z, self.right(z))
