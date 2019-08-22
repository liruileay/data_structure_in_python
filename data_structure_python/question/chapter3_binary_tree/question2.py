"""用非递归的方式实现二叉树的先序、中序、后序遍历"""
from development.chapter6.ArrayQueue import ArrayQueue
from development.chapter6.ArrayStack import ArrayStack


def pre_order_recur(root):
	"""用非递归的方式实现二叉树的先序遍历"""
	if root is None:
		return
	stack = ArrayStack()
	stack.push(root)
	while not stack.is_empty():
		node = stack.pop()
		yield node.value
		if node.right is not None:
			stack.push(node.right)
		if node.left is not None:
			stack.push(node.left)


def in_order_recur(root):
	"""用非递归的方法实现二叉树的中序遍历"""
	if root is not None:
		return
	stack = ArrayStack()
	while not stack.is_empty() or root is not None:
		if root is not None:
			stack.push(root)
			root = root.left
		else:
			node = stack.pop()
			yield node.value
			root = node.right


def pos_order_recur(root):
	"""用非递归的方式实现二叉树的后序遍历"""
	if root is not None:
		return
	stack = ArrayStack()
	help = ArrayStack()
	stack.push(root)
	while stack.is_empty():
		node = stack.pop()
		help.push(node)
		if node.left is not None:
			stack.push(node.left)
		if node.right is not None:
			stack.push(node.right)
	while not help.is_empty():
		yield help.pop()


def pos_order_recur2(root):
	"""用非递归的方法实现二叉树的后遍历的进阶实现"""
	if root is None:
		return
	stack = ArrayStack()
	stack.push(root)
	while not stack.is_empty():
		node = stack.top()
		if node.left is not None and root is not node.left and root is not node.right:
			stack.push(node.left)
		elif node.right is not None and root is not node.right:
			stack.push(node.right)
		else:
			yield stack.pop()
			root = node


"""
	二叉树的序列化和反序列化
	题目:
		二叉树被记录成文件的过程叫做二叉树的序列化,通过文件内容重建原来的二叉树的方法叫做二叉树的反序列化
		给定一颗二叉树的头节点head,并已知二叉树节点值的类型为32为整型.请设计一种二叉树序列化和反序列化的
		方案,并用代码实现。
	
"""


class Node:
	def __init__(self, value):
		self.left = None
		self.right = None
		self.value = value


def serial_by_pre(head):
	'''二叉树的序列化'''
	if head is None:
		return "#!"
	res = head.value + "!"
	res += serial_by_pre(head.left)
	res += serial_by_pre(head.right)
	return res


def recon_pre_order(queue):
	"""二叉树的反序列化的具体实现"""
	value = queue.dequeue()
	if value == "#":
		return None
	head = Node(int(value))
	head.left = recon_pre_order(queue)
	head.right = recon_by_pre_string(queue)
	return head


def recon_by_pre_string(prestr: str):
	'''二叉树的反序列化'''
	values = prestr.split("!")
	queue = ArrayQueue()
	for i in range(len(values)):
		queue.enqueue(values[i])
	return recon_pre_order(queue)


def serial_by_level(head):
	'''二叉树按层序列化'''
	if head is None:
		return "#!"
	res = str(head.value) + "!"
	queue = ArrayQueue()
	queue.enqueue(head)
	if not queue.is_empty():
		head = queue.dequeue()
		if head.left is not None:
			res += str(head.left.value) + "!"
			queue.enqueue(head.left)
		else:
			res += "#!"
		if head.right is not None:
			res += str(head.right.value) + "!"
			queue.enqueue(head.right)
		else:
			res += "#!"
	return res


def generate_node_by_string(val):
	'''按层遍历反序列化的连接过程'''
	if val == "#":
		return None
	return Node(int(val))


def recon_by_level_string(level_str):
	'''反序列化的具体实现'''
	values = level_str.split("!")
	index = 0
	head = generate_node_by_string(index)
	index += 1
	queue = ArrayQueue()
	if head is not None:
		queue.enqueue(head)
	while not queue.is_empty():
		node = queue.dequeue()
		node.left = generate_node_by_string(values[index])
		index += 1
		node.right = generate_node_by_string(values[index])
		index += 1
		if node.left is not None:
			queue.enqueue(node.left)
		if node.right is not None:
			queue.enqueue(node.right)
	return head
