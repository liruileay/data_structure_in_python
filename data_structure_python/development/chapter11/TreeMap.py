from development.chapter10.MapBase import MapBase
from development.chapter8.LinkedBinaryTree import LinkedBinaryTree


class TreeMap(LinkedBinaryTree, MapBase):
	'''基于链式二叉树的链式搜索二叉树的实现'''
	
	class Position(LinkedBinaryTree.Position):
		def key(self):
			'''返回对应的key值'''
			return self.element()._key
		
		def value(self):
			'''返回元素对应的元素值'''
			return self.element()._value
	
	def _subtree_search(self, p, k):
		'''p的子树下返回key值为k的搜索二叉树的节点 二分查找'''
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
	
	def __iter__(self):
		'''将所有节点设置为一个可迭代的对象'''
		p = self.first()
		while p is not None:
			yield p.key()
			p = self.after(p)
	
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
	
	def _rebalance_insert(self, p):
		"""Call to indicate that position p is newly added."""
		pass
	
	def _rebalance_delete(self, p):
		"""Call to indicate that a child of p has been removed."""
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
