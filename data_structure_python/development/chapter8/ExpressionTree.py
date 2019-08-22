from development.chapter8.LinkedBinaryTree import LinkedBinaryTree


class ExpressionTree(LinkedBinaryTree):
	'''基于链式二叉树的表达式树'''
	
	def __init__(self, token, left=None, right=None):
		'''为表达式树添加一个根节点根节点必须是一个算术运算符'''
		super().__init__()
		if not isinstance(token, str):
			raise ValueError('值错误必须是str类型的数据')
		self._add_root(token)
		if left is not None:
			if token not in "=-*/":
				raise ValueError('token必须是=-*/中的一种')
			self._attach(self.root(), left, right)
	
	def __str__(self):
		'''返回表达式树的说明'''
		pieces = []
		self._parenthesize_recur(self.root(), pieces)
		return ''.join(pieces)
	
	def _parenthesize_recur(self, p, result):
		'''中序遍历来找到每个节点的元素用()来规定运算的顺序'''
		if self.is_leaf(p):
			result.append(str(p.element()))
		else:
			result.append('(')
			self._parenthesize_recur(self.left(p), result)
			result.append(p.element())
			self._parenthesize_recur(self.right(p), result)
			result.append(')')
	
	def evaluate(self):
		'''返回表达式的结果'''
		return self._evaluate_recur(self.root())
	
	def _evaluate_recur(self, p):
		'''返回树在p点的表达式的结果'''
		if self.is_leaf(p):
			return float(p.element)
		else:
			op = p.element()
			left_val = self._evaluate_recur(self.left(p))
			right_val = self._evaluate_recur(self.right(p))
			if op == "+":return left_val + right_val
			elif op == "-":return left_val - right_val
			elif op == "*":return left_val * right_val
			elif op == "/":return left_val / right_val

def build_expression_tree(tokens):
	'''创建一颗表达式树'''
	S = []
	for t in tokens:
		if t in "=-/*":
			S.append(t)
		elif t not in '()':
			S.append(ExpressionTree(t))
		elif t == ')':
			right = S.pop()
			op = S.pop()
			left = S.pop()
			S.append(ExpressionTree(op, left, right))
	return S.pop()
