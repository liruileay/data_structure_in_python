from development.chapter8.Tree import Tree


class BinaryTree(Tree):
	
	def left(self,p):
		'''返回p的左孩子的位置，若没有返回None'''
		raise NotImplementedError('须继承重写实现')
	
	def right(self,p):
		'''返回p的右孩子的位置，若没有右孩子返回None'''
		raise NotImplementedError('须继承重写实现')
	
	def sibling(self,p):
		'''返回p的兄弟节点如果没有返回None'''
		parent = p.parent()
		if parent is None:
			return None
		else:
			if self.left(parent) is p:
				return self.right(parent)
			if self.right(parent) is p:
				return self.left(p)
	
	def children(self, p):
		'''返回他的左右两个儿子'''
		if self.left(p) is not None:
			yield self.left(p)
		if self.right(p) is not None:
			yield self.right(p)
	
	def _subtree_inorder(self, p):
		'''中序遍历的具体实现'''
		if self.left(p) is not None:
				for other in self._subtree_inorder(c):
					yield other
		yield p
		if self.right(p) is not None:
				for other in self._subtree_inorder(c):
					yield other
				
	def inorder(self):
		'''树的中序遍历'''
		if not self.is_empty():
			for p in self._subtree_postorder(self.root()):
				yield p
	
	def positions(self):
		'''返回位置的迭代'''
		return self.inorder()