from development.chapter7.LinkedQueue import LinkQueue


class Tree(object):
	'''一个抽象的树类本类的存在是其他子类用于继承的基础'''
	
	class Position(object):
		'''树的位置的抽象方法'''
		
		def element(self):
			'''返回该节点的元素'''
			raise NotImplementedError('必须被子类重写否则不能实现')
		
		def __eq__(self, other):
			raise NotImplementedError('必须被子类重写否则不能实现')
		
		def __ne__(self, other):
			raise NotImplementedError('必须被子类重写否则不能实现')
	
	def root(self):
		'''返回根节点'''
		raise NotImplementedError('必须被子类重写否则不能实现')
	
	def parent(self, p):
		'''返回该位置的父节点'''
		raise NotImplementedError('必须被子类重写否则不能实现')
	
	def num_children(self, p):
		'''返回该位置p的孩子的个数'''
		raise NotImplementedError('必须被子类重写否则不能实现')
	
	def children(self, p):
		'''表示p的子节点的迭代先是左孩子后是右孩子'''
		raise NotImplementedError('必须被子类重写否则不能实现')
	
	def __len__(self):
		'''返回树的元素个数'''
		raise NotImplementedError('必须被子类重写否则不能实现')
	
	def is_root(self, p):
		'''判断是不是根节点'''
		return self.root() == p
	
	def is_leaf(self, p):
		'''判断是不是叶节点'''
		return self.num_children(p) is None
	
	def is_empty(self):
		'''判断该树是不是为空'''
		return len(self) == 0
	
	def depth(self, p):
		'''计算节点p的深度'''
		if self.is_root(p):
			return 0
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
	
	def __iter__(self):
		'''实现树的遍历'''
		for p in self.positions():
			yield p._element
	
	def preorder(self):
		'''树的先序遍历'''
		if not self.is_empty():
			for p in self._subtree_preorder(self.root()):
				yield p
	
	def _subtree_preorder(self,p):
		'''在该位置生成先序遍历的迭代器'''
		yield p
		for c in self.children(p):
			for other in self._subtree_preorder(c):
				yield other
				
	def positions(self):
		'''返回树的所有节点'''
		# raise NotImplementedError('必须被子类重写否则不能实现')
		return self.preorder()
	
	def postorder(self):
		'''后序遍历'''
		if self.is_empty():
			for p in self._subtree_postorder(self.root()):
				yield p
	
	def _subtree_postorder(self,p):
		'''后序遍历实现迭代器'''
		for c in self.children(p):
			for other in self._subtree_postorder(c):
				yield other
		yield p
		
	def breadthfirst(self):
		'''广度优先遍历的实现'''
		if not self.is_empty():
			fringe = LinkQueue()
			fringe.enqueue(self.root())
			while not fringe.is_empty():
				p = fringe.dequeue()
				yield p
				for c in self.children(p):
					fringe.enqueue(c)
	

# def p(root):
# 	'''先序遍历'''
# 	if root is None:
# 		return
# 	stack = []
# 	stack.append(root)
# 	while stack:
# 		node = stack.pop()
# 		yield node.element()
# 		if node.right:
# 			stack.append(node.right)
# 		if node.left:
# 			stack.append(node.left)
#
# def f(root):
# 	'''后序遍历'''
# 	if root is None:
# 		return
# 	stack = []
# 	stack.append(root)
# 	result = []
# 	while stack:
# 		node = stack.pop()
# 		result.append(node)
# 		if node.right:
# 			stack.append(node.right)
# 		if node.left:
# 			stack.append(node.left)
# 	while result:
# 		yield result.pop()
#
# def l(root):
# 	'''中序遍历'''
# 	if root is None:
# 		return
# 	stack = []
# 	stack.append(root)
# 	node = root
# 	while stack:
# 		if node:
# 			stack.append(node.left)
# 			node = node.left
# 		else:
# 			node = stack.pop()
# 			yield node
# 			stack.append(node.right)