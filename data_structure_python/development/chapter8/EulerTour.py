'''模板方法模式'''

class EulerTour(object):
	'''一个为欧拉遍历实现的基类'''
	def __init__(self,tree):
		'''给定一个遍历的模板'''
		self._tree = tree
	
	def tree(self):
		'''查看这个树'''
		return self._tree
	
	def execute(self):
		'''完成遍历并返回遍历后的结果‘'''
		if len(self._tree):
			return self._tour(self._tour.root(),0,[]) # 头节点的位置
	
	def _tour(self,p,d,path):
		'''
		对根位于p节点的子树进行遍历
		p:    表示当前节点的位置
		d:    p在当前节点中的深度
		path: 从路径根到p的路径上的子节点列表
		'''
		self._hook_previsit(p,d,path)
		results = []
		path.append(0)
		for c in self._tree.children(p):
			results.append(self._tour(c,d+1,path))
			path[-1] +=1
		path.pop()
		answer = self._hook_postvisit(p,d,path,results)
		return answer
		
		
	
	def _hook_previsit(self,p,d,path):
		"""
		在子树调用前调用这个函数   ->表示先访问的出现
		p:      当前节点在树上面的位置
		d:      当前节点的深度
		path:   索引的列表
		"""
		pass
	
	def _hook_postvisit(self,p,d,path,result):
		'''
		在子树调用后调用这个函数    ->表示后访问的实现
		p:      当前节点在书上面的位置
		d:      表示当前节点的深度
		path:   表示索引的列表
		result: 以p的子树后序遍历的返回值作为列表对象
		'''
		pass
	