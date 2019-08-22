"""将搜索二叉树转换为双向链表"""
from development.chapter6.ArrayQueue import ArrayQueue


class Node(object):
	def __init__(self, data):
		self.value = data
		self.left = None
		self.right = None


def in_order_to_queue(head, queue):
	"""将二叉树按照中序遍历的顺序存放在queue中"""
	if head is None:
		return head
	in_order_to_queue(head.left, queue)
	queue.enqueue(head)
	in_order_to_queue(head.right, queue)


def concert1(head):
	"""将搜索二叉树转化为双向链表的具体实现"""
	# left相当于parent证指针 right相当于next指针
	queue = ArrayQueue()
	in_order_to_queue(head, queue)
	if queue.is_empty():
		return head
	head = queue.dequeue()
	pre = head
	pre.left = None
	while not queue.is_empty():
		cur = queue.dequeue()
		pre.right = cur
		cur.left = pre
		pre = cur
	pre.right = None
	return head


def process(head):
	"""对链表的处理过程"""
	if head is None:
		return None
	leftE = process(head.left)  # 处理左子树
	rightE = process(head.right)  # 处理右子树
	leftS = leftE.right if leftE is not None else None  # 判断左子树是否是值的
	rightS = rightE.right if rightE is not None else None  # 判断右子树是不是有值的
	if leftE is not None and rightE is not None:  # 第一种情况左右两个子树都是有值的
		leftE.right = head
		head.left = leftE
		head.right = rightS
		head.left = leftS
		return rightE
	elif leftE is not None:  # 第二种情况左子树有值右子树没有值
		leftE.right = head
		head.left = leftE
		head.right = leftS
		return head
	elif rightE is not None:  # 第三种情况右子树有值左子树没有值
		head.right = rightS
		rightS.left = head
		rightE.right = head
		return rightE
	else:  # 最后一种情况两个子树都是没有值的
		head.right = head
		return head


def convert2(head):
	"""将搜索二叉树转化为双向链表的具体实现"""
	if head is None:
		return None
	last = process(head)
	head = last.right
	last.right = None
	return head
