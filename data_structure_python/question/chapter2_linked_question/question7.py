"""
判断一个链表是不是回文结构 给定一个链表
例如:
	1 ->2 ->1 返回True
	1 ->2 ->2 ->1 返回为True
	15 -> 6 ->15 返回True
	1 -> 2 ->3 返回False
	
"""
from development.chapter6.ArrayStack import ArrayStack


def is_palindrome1(head):
	"""判断一个链表是不是会问结构  --->将整个压入栈中比较"""
	stack = ArrayStack()
	cur = head
	while cur is not None:
		stack.push(cur)
		cur = cur.next
	while head is not None:
		if head.value != stack.pop().value:
			return False
		head = head.next
	return True


def is_palindrome2(head):
	"""判断一个链表是不是回文结构 --->将后面的一半压入栈中比较"""
	if head is None or head.next is None:
		return True
	right = head.next
	cur = head
	while cur.next is not None and cur.next.next is not None:
		right = right.next
		cur = cur.next.next
	stack = ArrayStack()
	while right is not None:
		stack.push(right)
		right = right.next
	while not stack.is_empty():
		if head.value != stack.pop().value:
			return False
		head = head.next
	return True


def is_palindrome3(head):
	"""判断一个链表是不是回文结构  -->将后面的一半反转比较后重连"""
	
	if head is None or head.next is None:
		return True
	n1 = head
	n2 = head
	while n2.next is not None and n2.next.next is not None:
		n1 = n1.next
		n2 = n2.next.next
	n2 = n1.next
	n1.next = None
	while n2 is not None:
		n3 = n2.next
		n2.next = n1
		n1 = n2
		n2 = n3
	n3 = n1
	n2 = head
	res = True
	while n1 is not None and n2 is not None:
		if n1.value != n2.value:
			res = False
			break
		n1 = n1.next
		n2 = n2.next
	n1 = n3.next
	n3.next = None
	while n1 is not None:
		n2 = n1.next
		n1.next = n3
		n3 = n1
		n1 = n2
	return res
