from development.chapter8 import BinaryEulerTour


class BinaryLayout(BinaryEulerTour):
	'''为二叉树的每个节点定义一个作标
		Setx        表示原来的元素支持设置x的值
		Sety        表示原来的元素支持设置y的值
	'''
	
	def __init__(self, tree):
		super().__init__(tree)
		self._count = 0
	
	def _hook_invisit(self, p, d, path):
		'''
		中序遍历给元素添加一个x和y的一个作标属性
		p:      表示当前节点的位置
		d:      表示当前树的深度
		'''
		p.element().setX(self._count)
		p.element().setY(d)
		self._count += 1
