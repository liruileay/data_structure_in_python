from development.chapter11.TreeMap import TreeMap


class SplayTreeMap(TreeMap):
	'''基于链式二叉树的伸展树'''
	
	def _splay(self, p):
		'''对节点进行伸展操作'''
		while p != self.root():
			parent = self.parent(p)
			grand = self.parent(parent)
			if grand is None:
				self._rotate(p)
			elif (parent == self.left(grand)) == (p == self.left(parent)):
				self._rotate(parent)
				self._rotate(p)
			else:
				self._rotate(p)
				self._rotate(p)
	
	def _rebalance_delete(self, p):
		'''删除元素后进行树的伸展操作'''
		self._splay(p)
	
	def _rebalance_access(self, p):
		'''访问的时候进行树的伸展操作'''
		self._splay(p)
	
	def _rebalance_insert(self, p):
		'''插入新的节点后进行树的伸展操作'''
		self._splay(p)
