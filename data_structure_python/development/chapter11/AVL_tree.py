from collections import MutableMapping

from development.chapter7.LinkedQueue import LinkQueue


class AVLTreeMap(MutableMapping):
	'''AVL树的实现'''
	
	class _Node:
		__slots__ = '_element', '_height', '_parent', '_left', '_right'
		
		def __init__(self, element, parent=None, left=None, right=None):
			"""
			_element:       表示节点的元素属性
			_height:        表示该节点的高度
			_parent:        表示该节点的父节点
			_left:          表示该节点的左孩子
			_right:         表示该节点的右孩子
			"""
			self._height = 0
			self._element = element
			self._parent = parent
			self._left = left
			self._right = right
		
		def left_height(self):
			return self._left._height if self._left is not None else 0
		
		def right_height(self):
			return self._right._height if self._right is not None else 0
	
	class _Item:
		__slots__ = '_key', '_value'
		
		def __init__(self, k, v):
			"""
			_key:           表示节点元素元素的key值
			_value:         表示节点元素的value值
			"""
			self._key = k
			self._value = v
		
		def __eq__(self, other):
			return self._key == other._key
		
		def __ne__(self, other):
			return self._key != other._key
		
		def __lt__(self, other):
			return self._key < other._key
	
	class Position:
		def __init__(self, container, node):
			self._container = container
			self._node = node
		
		def element(self):
			return self._node._element
		
		def __eq__(self, other):
			return type(other) is type(self) and type(other._node) is type(self._node)
		
		def key(self):
			return self.element()._key
		
		def value(self):
			return self.element()._value
	
	def _vaildate(self, p):
		"""校验节点p是否符合要求如果符合要求就返回p位置的节点如果不符合要求就报错"""
		if not isinstance(p, self.Position):
			raise TypeError('p位置不是Position的一个实例')
		if p._container is not self:
			raise TypeError('p位置是Position的实例但是不是AVL树的子节点')
		if p._node._parent is p._node:
			raise ValueError('节点为空没有意义')
		return p._node
	
	def _make_position(self, node):
		"""找到节点所在的位置"""
		return self.Position(self, node)._node if node is not None else None
	
	def __init__(self):
		"""
		_root:      表示AVL树的头节点
		_size:      记录AVL树的节点的个数
		"""
		self._root = None
		self._size = 0
	
	def __len__(self):
		return self._size
	
	def __iter__(self):
		'''将所有节点设置为一个可迭代的对象'''
		p = self.first()
		while p is not None:
			yield p.key()
			p = self.after(p)
	
	def is_root(self, p):
		self._vaildate(p)
		return self.root() is p
	
	def num_children(self, p):
		self._vaildate(p)
		count = 0
		if self.left(p) is not None:
			count += 1
		if self.right(p) is not None:
			count += 1
	
	def is_leaf(self, p):
		self._vaildate(p)
		return self.num_children(p) == 0
	
	def is_empty(self):
		return len(self) == 0
	
	def left(self, p):
		node = self._vaildate(p)
		return self._make_position(node._left)
	
	def right(self, p):
		node = self._vaildate(p)
		return self._make_position(node._right)
	
	def parent(self, p):
		node = self._vaildate(p)
		return self._make_position(node._parent)
	
	def root(self):
		return self._make_position(self._root)
	
	def sibling(self, p):
		self._vaildate(p)
		parent = p.parent()
		if parent is None:
			return None
		else:
			if self.left(parent) is p:
				return self.right(parent)
			elif self.right(parent) is p:
				return self.left(parent)
	
	def children(self, p):
		self._vaildate(p)
		if self.left(p) is not None:
			yield self.left(p)
		if self.right(p) is not None:
			yield self.right(p)
	
	def _subtree_inorder(self, p):
		"""中序遍历的具体实现过程"""
		self._vaildate(p)
		if self.left(p) is not None:
			for other in self._subtree_inorder(self.left(p)):
				yield other
		yield p
		if self.right(p) is not None:
			for other in self._subtree_inorder(self.right(p)):
				yield other
	
	def inorder(self):
		"""对树进行中序遍历"""
		if not self.is_empty():
			for p in self._subtree_inorder(self.root()):
				yield p
	
	def _subtree_preorder(self, p):
		self._vaildate(p)
		yield p
		for c in self.children(p):
			for other in self._subtree_preorder(c):
				yield other
	
	def preorder(self):
		"""对AVL树进行先序遍历"""
		if not self.is_empty():
			for p in self._subtree_preorder(self.root()):
				yield p
	
	def _subtree_postorder(self, p):
		self._vaildate(p)
		for c in self.children(p):
			for other in self._subtree_preorder(c):
				yield other
		yield p
	
	def postorder(self):
		"""对AVL树实现后序遍历"""
		if not self.is_empty():
			for p in self._subtree_postorder(self.root()):
				yield p
	
	def breadthfirst(self):
		"""广度优先遍历"""
		if self.is_empty():
			return None
		fringe = LinkQueue()
		fringe.enqueue(self.root())
		while not fringe.is_empty():
			p = fringe.dequeue()
			yield p
			for c in self.children(p):
				fringe.enqueue(c)
	
	def positions(self):
		return self.inorder()
	
	def depth(self, p):
		"""返回树的深度"""
		if self.is_root(p):
			return 1
		return 1 + self.depth(self.parent(p))
	
	def _height1(self):
		'''计算树的高度等于该树页节点的深度的最大值'''
		return max(self.depth(p) for p in self.positions() if self.is_leaf(p))
	
	def _height2(self, p):
		'''返回p节点的高度该树的所有子节点高度的最大值加一'''
		if self.is_leaf(p):
			return 0
		return 1 + max(self._height2(c) for c in self.children(p))
	
	def height(self, p=None):
		'''计算整个树或者给定一个树的高度'''
		if p is None:
			p = self.root()
		return self._height2(p)
	
	def _add_root(self, e):
		'''为树添加一个根节点'''
		if self.root() is not None: raise ValueError('头节点为空不能添加')
		self._root = self._Node(e)
		self._size += 1
		return self.Position(self, self._root)
	
	def _add_left(self, p, e):
		"""给树添加一个左孩子"""
		node = self._vaildate(p)
		if self.left(p) is not None: raise ValueError('左孩子为空不能添加')
		self._size += 1
		node._left = self._Node(e, node)
		return self._make_position(node._left)
	
	def _add_right(self, p, e):
		"""给叔添加一个右孩子"""
		node = self._vaildate(p)
		if self.right(p) is not None: raise ValueError('右孩子不为空不能添加')
		self._size += 1
		node._right = self._Node(e, node)
		return self._make_position(node._right)
	
	def _replace(self, p, e):
		"""替换p节点的element元素的值并且返回该节点原来的元素值"""
		node = self._vaildate(p)
		old = node._element
		node._element = e
		return old
	
	def _delete(self, p):
		"""删除p节点并且返回节点p的元素值"""
		node = self._vaildate(p)
		if self.num_children(node) == 2: raise ValueError('该节点连个孩子不能删除')
		child = node._left if node._left is not None else node._right
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
		self._size -= 1
		node._parent = node
		return node._element
	
	def _attach(self, p, t1, t2):
		"""将树t1和树t2连接到p节点上面"""
		node = self._vaildate(p)
		if not self.is_leaf(p): raise ValueError('只有叶节点才能连接两个子树')
		if not type(p) is type(t1) is type(t2): raise TypeError('只有相同类型的是才能连接在一起')
		self._size += len(t1) + len(t2)
		if not t1.is_empty():
			t1._root._parent = node
			node._left = t1._root
			t1._root = None
			t1._size = 0
		if not t2.is_empty():
			t2._root._parent = node
			node._right = t2._root
			t2._root = None
			t2._size = 0
	
	def _subtree_search(self, p, k):
		'''采用二分查找的方法快速查找出key值等于k的节点的位置'''
		if k == p.key():
			return p
		if k < p.key():
			if self.left(p) is not None:
				return self._subtree_search(self.left(p), k)
		if k > p.key():
			if self.right(p) is not None:
				return self._subtree_search(self.right(p), k)
		return p
	
	def _subtree_first_position(self, p):
		'''返回整个搜索二叉树的第一个节点 --->key值最小的节点也是整个搜素二叉树最左边的位置'''
		walk = p
		while self.left(walk) is not None:
			walk = self.left(walk)
		return walk
	
	def _subtree_last_position(self, p):
		'''返回整个搜索二叉树的最后一个节点 --->key值最大的节点越是整个搜索二叉树最右边的位置'''
		walk = p
		while self.right(walk) is not None:
			walk = self.right(walk)
		return walk
	
	def first(self):
		'''返回搜索树的第一个节点key值是最小的'''
		return self._subtree_first_position(self.root()) if len(self) > 0 else None
	
	def last(self):
		'''返回的节点是整个数上面key值最大的节点位置'''
		return self._subtree_last_position(self.root()) if len(self) > 0 else None
	
	def before(self, p):
		'''返回p前面的节点      p的前继节点'''
		self._vaildate(p)
		if self.left(p) is not None:
			return self._subtree_last_position(self.left(p))
		else:
			walk = p
			above = self.parent(walk)
			while above is not None and walk == self.left(above):
				walk = above
				above = self.parent(walk)
			return above
	
	def after(self, p):
		'''位置p后面的节点      p的后继节点'''
		self._vaildate(p)
		if self.right(p) is not None:
			return self._subtree_first_position(self.right(p))
		else:
			walk = p
			above = self.parent(walk)
			while above is not None and walk == self.right(walk):
				walk = above
				above = self.parent(walk)
			return above
	
	def find_min(self):
		'''找到key值最小的一个节点'''
		if self.is_empty():
			return None
		p = self.first()
		return (p.key(), p.value())
	
	def find_ge(self, k):
		'''找到比k大的第一个节点 后面的节点'''
		if self.is_empty():
			return None
		else:
			p = self.find_position(k)
			if self.keys() < k:
				p = self.after(p)
			return (p.key(), p.value())
	
	def find_range(self, start, stop):
		'''找到key值介于start和stop的节点'''
		if not self.is_empty():
			if start is None:
				p = self.first()
			else:
				p = self.find_position(start)
				if p.key() < start:
					p = self.after(p)
			while p is not None and (stop is None or stop > p.key()):
				yield (p.key(), p.value())
				p = self.after(p)
	
	def find_position(self, k):
		'''找到key值为k对应的节点'''
		if self.is_empty():
			return None
		else:
			p = self._subtree_search(self.root(), k)
			self._rebalance_access(p)
			return p
	
	def __getitem__(self, k):
		'''获取key为k的元素的value值'''
		if self.is_empty():
			raise KeyError('没有这样的k')
		else:
			p = self._subtree_search(self.root(), k)
			self._rebalance_access(p)
			if p.key() != k:
				raise KeyError('没有这样的k值')
			return p.value()
	
	def __setitem__(self, k, v):
		'''设置key为k的值'''
		if self.is_empty():
			leaf = self._add_root(self._Item(k, v))
		else:
			p = self._subtree_search(self.root(), k)
			self._rebalance_access(p)
			if k == p.key():
				p.element()._value = v
				self._rebalance_access(p)
				return
			else:
				item = self._Item(k, v)
				if p.key() < k:
					leaf = self._add_left(p, item)
				else:
					leaf = self._add_right(p, item)
		self._rebalance_insert(leaf)
	
	def delete(self, p):
		'''删除p位置节点'''
		self._vaildate(p)
		if self.left(p) and self.right(p):
			replacement = self._subtree_last_position(self.left(p))
			self._replace(p, replacement.element())
			p = replacement
		parent = self.parent(p)
		self._delete(parent)
	
	def __delitem__(self, k):
		if not self.is_empty():
			p = self._subtree_search(self.root(), k)
			if p.key() == k:
				self.delete(p)
				return
			self._rebalance_access(p)
		raise KeyError('没有这样的k值')
	
	def _rebalance_access(self, p):
		"""Call to indicate that position p was recently accessed."""
		pass
	
	def _relink(self, parent, child, make_left_child):
		'''重连父节点和子节点允许子节点为空'''
		if make_left_child:
			parent._left = child
		else:
			parent._right = child
		if child is not None:
			child._parent = parent
	
	def _rotate(self, p):
		'''重新连接父节点和字节 '''
		'''
				b            a
			   / \          / \
			  a   t2      t0   b
			 / \              / \
			t0  t1           t1  t2
			将整个二叉树进行旋转 达到平衡并且具有搜索二叉树的性质
		'''
		x = p._node
		y = x._parent
		z = y._parent
		if z is None:
			self._root = x
			x._parent = None
		else:
			self._relink(z, x, y == z._left)
		if x == y._left:
			self._relink(y, x._right, True)
			self._relink(x, y, False)
		else:
			self._relink(y, x._left, False)
			self._relink(x, y, True)
	
	def _restructure(self, x):
		'''对二叉树进行重构让其成为平衡二叉树'''
		"""
		二叉树重构前的数结构图:
			(1)	z=a             (2) z=c       (3) z=a           (4) z=c
		       /  \                /  \          /  \              /  \
		      t0  y=b             y=b  t3       t0   y=c          y=a  t3
		         /  \            /  \               /  \         /  \
		        t1  x=c         x=a  t2            x=b  t3      t0   x=b
		           /  \        /  \               /  \              /  \
		          t2  t3      t0  t1             t1  t2            t1  t2
		其中(1)和(2)经历一次重构 (3)和(4)经历两次重构
        二叉树重构后的数的结构图:
               b
            /    \
          a       c
         / \     /  \
        t0  t1  t2  t3
        """
		y = self.parent(x)
		z = self.parent(y)
		if (x == self.right(y)) == (y == self.right(z)):
			self._rotate(y)
			return y
		else:
			self._rotate(x)
			self._rotate(x)
			return x
	
	def _recompute_height(self, p):
		'''数p的节点的高度等于p左子树的高度和右子树高度的最大值加一'''
		p._node._height = 1 + max(p._node.left._height(), p._node.right._height())
	
	def _isbalanced(self, p):
		'''判读p这颗树是否平衡 左子树和右子树的高度差不大于1那么平衡'''
		return abs(p._node.left_height() - p._node.right_height()) <= 1
	
	def _tall_child(self, p, favorfelt=False):
		'''返回左右树中高度高的那个，如果一样高就返回左子树'''
		if p._node.left_height() + (1 if favorfelt else 0) > p._node.right_height():
			return self.left(p)
		else:
			return self.right(p)
	
	def _tall_grandchild(self, p):
		'''得到子树的子树的高度'''
		child = self._tall_child(p)
		alignment = (child == self.left(p))
		return self._tall_child(child, alignment)
	
	def _rebalance(self, p):
		'''将整棵树调整成为一颗AVL树'''
		while p is not None:
			old_height = p._node._height
			if not self._isbalanced(p):
				p = self._restructure(self._tall_grandchild(p))
				self._recompute_height(self.left(p))
				self._recompute_height(self.right(p))
			self._recompute_height(p)
			if p._node._height == old_height:
				p = None
			else:
				p = self.parent(p)
	
	def _rebalance_insert(self, p):
		'''在每次插入新的节点后都重构保持AVL树的平衡'''
		self._rebalance(p)
	
	def _rebalance_delete(self, p):
		'''在每次删除后都重构保持AVL树的平衡'''
		self._rebalance(p)
