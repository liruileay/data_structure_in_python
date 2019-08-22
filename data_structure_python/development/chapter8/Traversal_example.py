'''树的遍历对数进行序列化'''


def preorder_indent(T, p, d):
	"""中序遍历来描述一个列表d表示数的深度"""
	print(2*d*'' + str(p.element()))
	for c in T.children():
		preorder_indent(T,c,d+1)


def preorder_lable(T, p, d, path):
	'''用于更加形象的打印先序遍历path表示了树的层数'''
	lable = ".".join(str(j + 1) for j in path)
	print(2 * d * '' + lable, p.element())
	path.append(0)
	for c in T.children(p):
		preorder_lable(T, c, d + 1, path)
		path[-1] += 1
	path.pop()


def parentthesize(T, p):
	'''输出树的附加说明和字符串表示函数'''
	print(p.element(), end='')
	if not T.is_leaf():
		first_time = True
		for c in T.children(p):
			sep = ' (' if first_time else ','
			print(sep, end='')
			first_time = False
			parentthesize(T, c)
		print(')', end='')

def disk_space(T, p):
	'''树磁盘空间的函数其中space表示了该元素在这个地方的空间使用'''
	subtotal = p.element().space()
	for c in T.children(p):
		subtotal +=disk_space(T,c)
	return subtotal

