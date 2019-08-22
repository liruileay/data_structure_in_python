"""单个链表生成相加链表
题目:
	假设链表中每一个节点的值都在0-9之间,那么链表整体就可以代表一个整数
	例如:9->3->7,可以代表整数937
	给定两个这种链表的头节点head1和head2,请生成代表两个整数相加值的结果链表
	例如:链表1为9->3->7,链表2为6->3,最后生成新的结果链表为1->0->0->0.
	
"""
from development.chapter6.ArrayStack import ArrayStack


class Node(object):
	"""链表节点的初始化"""
	
	def __init__(self, data):
		self.value = data
		self.next = None


def add_lists1(head1, head2):
	"""两个单链表的相加的具体实现"""
	s1 = ArrayStack()
	s2 = ArrayStack()
	while head1 is not None:
		s1.push(head1.value)
		head1 = head1.next
	while head2 is not None:
		s2.push(head2.value)
		head2 = head2.next
	ca = 0
	node = None
	while not s1.is_empty() or not s2.is_empty():
		n1 = 0 if s1.is_empty() else s1.pop()
		n2 = 0 if s2.is_empty() else s2.pop()
		n = n1 + n2 + ca
		pre = node
		node = Node(n % 10)
		node.next = pre
		ca = n // 10
	if ca == 1:
		pre = node
		node = Node(1)
		node.next = pre
	return node


def reverse_list(head):
	"""实现链表反转的逻辑"""
	pre = None
	while head is not None:
		next = head.next
		head.next = pre
		pre = head
		head = next


def add_list2(head1, head2):
	"""两个单链表相加的具体实现"""
	head1 = reverse_list(head1)
	head2 = reverse_list(head2)
	ca = 0
	c1 = head1
	c2 = head2
	node = None
	while c1 is not None or c2 is not None:
		n1 = 0 if c1 is None else c1.value
		n2 = 0 if c2 is None else c2.value
		n = n1 + n2 + ca
		pre = node
		node = Node(n % 10)
		node.next = pre
		ca = n // 10
		c1 = None if c1 is None else c1.next
		c2 = None if c2 is None else c2.next
	if ca == 1:
		pre = node
		node = Node(1)
		node.next = pre
	reverse_list(head1)
	reverse_list(head2)
	return node
