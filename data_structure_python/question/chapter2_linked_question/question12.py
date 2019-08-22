"""将单个链表的每k个节点之间逆序

"""
from development.chapter6.ArrayStack import ArrayStack


class Node(object):
	
	def __init__(self, data):
		self.value = data
		self.next = None


def resign1(stack, left, right):
	cur = stack.pop()
	if left is not None:
		left.next = cur
	while not stack.is_empty():
		next = stack.pop()
		cur.next = next
		cur = next
	cur.next = right
	return cur


def reverse_K_nodes1(head, K):
	'''将单个链表每隔K个节点逆序的具体实现'''
	if K < 2:
		return head
	stack = ArrayStack()
	new_head = head
	cur = head
	pre = None
	while cur is not None:
		next = cur.next
		stack.push(cur)
		if len(stack) == K:
			pre = resign1(stack, pre, next)
			new_head = cur if new_head is head else new_head
			cur = next
	return new_head


def resign2(left, start, end, right):
	pre = start
	cur = start.next
	while cur is not right:
		next = cur.next
		cur.next = pre
		pre = cur
		cur = next
	if left is not None:
		left.next = end
	start.next = right


def reverse_k_nodes2(head, K):
	'''将单个链表每隔k个节点逆序的具体实现'''
	if K < 2:
		return head
	cur = head
	pre = None
	count = 1
	while cur is not None:
		next = cur.next
		if count == K:
			start = head if pre is None else pre.next
			head = cur if pre is None else head
			resign2(pre, start, cur, next)
			pre = start
			count = 0
		count += 1
		cur = next
	return head
