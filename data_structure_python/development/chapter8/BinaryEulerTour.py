from development.chapter8.EulerTour import EulerTour


class BinaryEulerTour(EulerTour):
	'''欧拉遍历具体实现'''
	
	def _tour(self,p,d,path):
		'''
		更加具体表示了一个节点右多个孩子的情况
		p:          表示当前的位置
		d:          表示当前节点的深度
		path:       表示当前的索引列表
		:return:    返回当前节点下欧拉遍历的实现
		'''
		results = [None,None]
		self._hook_previsit(p,d,path)
		if self._tree.left(p) is not None:
			path.append(0)
			results[0] = self._tour(self._tree.left(p),d+1,path)
			path.pop()
		self._hook_invisit(p,d,path)
		if self._tree.right(p) is not None:
			path.append(1)
			results[1] = self._tour(self._tree.roght(p),d+1,path)
			path.pop()
		answer = self._hook_postvisit(p,d,path,results)
		return answer
	
	def _hook_invisit(self,p,d,path):
		pass