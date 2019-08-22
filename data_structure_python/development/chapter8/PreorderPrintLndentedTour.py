from development.chapter8.EulerTour import EulerTour


class PreorderPrintIndentedTour(EulerTour):
	'''子类生成树元素的缩进先序列表'''
	def _hook_previsit(self,p,d,path):
		print(2*d*'',str(p.element()))

class PreorderPrintIndentedLabledTour(EulerTour):
	'''EulerTour的子类生成树元素的标记和缩进先序列表'''
	def _hook_previsit(self,p,d,path):
		label = '.'.join(str(j+1) for j in path)
		print(2*d*' ' + label,p.element())


class ParentthesizeTour(EulerTour):
	'''用于打印树的附加说明'''
	def _hook_previsit(self,p,d,path):
		if path and path[-1] >0:
			print(', ',end='')
		print(p.element(),end='')
		if not self.tree().is_leaf(p):
			print(' (',end='')
	
	def _hook_postvisit(self,p,d,path,result):
		if not self.tree().is_leaf(p):
			print(')',end='')
			

class DiskSpaceTour(EulerTour):
	def _hook_postvisit(self,p,d,path,result):
		'''欧拉遍历计算树的磁盘空间'''
		return p.element().space() + sum(result)