from development.chapter11.TreeMap import TreeMap


class AVlTreeMap(TreeMap):
	'''实现一个AVL树'''
	
	class _Node(TreeMap._Node):
		'''给原来的二叉树添加一个每个节点添加一个高度属性'''
		__slots__ = '_height'
		
		def __init__(self, element, parent=None, left=None, right=None):
			'''重写Node类添加高度属性并且提供查看高度的方法'''
			super().__init__(element, parent, left, right)
			self._height = 0
		
		def left_height(self):
			'''返回左树的高度'''
			return self._left._height if self._left is not None else 0
		
		def right_height(self):
			'''返回右数的高度'''
			return self._right._height if self._right is not None else 0
	
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
