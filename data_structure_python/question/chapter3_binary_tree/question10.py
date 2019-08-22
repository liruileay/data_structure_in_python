"""
二叉树安层打印于ZigZag打印
	题目: 给定一颗树的头节点head,分别实现安层打印和ZigZag打印二叉树的函数
	
"""
from development.chapter6.Double_ArrayQueue import DoubleArrayQueue
from development.chapter7.LinkedQueue import LinkedQueue


def print_by_level(head):
	'''二叉树按层打印'''
	if head is None:
		return
	queue = LinkedQueue()
	level = 1
	last = head
	nLast = None
	queue.enqueue(head)
	print("Level{]".format(level), end = ":")
	while not queue.is_empty():
		head = queue.dequeue()
		print(head.value, end = "")
		if head.left is not None:
			queue.enqueue(head.left)
			nLast = head.left
		if head.right is not None:
			queue.enqueue(head.right)
			nLast = head.right
		if last is head and not queue.is_empty():
			print("\nLevel{}".format(level), end = ":")
			level += 1
			last = nLast
	print("Print Over")


def print_level_and_orientation(levle, lr):
	'''ZigZag打印的具体实现'''
	print("Level {] from".format(levle))
	print("left to right " if lr else "right to left ")
	
def print_by_ZigZag(head):
	'''zigzag打印二叉树'''
	dq = DoubleArrayQueue()
	level = 1
	lr = True
	last = head
	nLast = None
	dq.add_first(head)
	print_level_and_orientation(level, lr)
	level += 1
	while not dq.is_empty():
		if lr:
			head = dq.delete_first()
			if head.left is not None:
				nLast = head.left if nLast is None else nLast
				dq.add_last(head.left)
			if head.right is not None:
				nLast = head.right if nLast is None else nLast
				dq.add_last(head.right)
		else:
			head = dq.delete_last()
			if head.right is not None:
				nLast = head.right if nLast is None else nLast
				dq.add_first(head.right)
			if head.left is not None:
				nLast = head.left if nLast is None else nLast
				dq.add_first(head.left)
		print(head.value)
		if head is last and not dq.is_empty():
			lr = False if lr else True
			last = nLast
			nLast = None
			print("")
			print_level_and_orientation(level, lr)
	print("Print Over")
