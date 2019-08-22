"""
在单链表中删除指定的值的节点
	给定一个链表的头节点head和一个整数num,请实现函数将值为num的节点全部删除
	例如:链表为1->2->3->4->None ,num=3 链表调节后为: 1->2->4->None
"""
from development.chapter6.ArrayStack import ArrayStack


def remove_value1(head, num):
	"""删除指定值的节点"""
	stack = ArrayStack()
	while head is not None:
		if head.value != num:
			stack.push(head)
		head = head.next
	while not stack.is_empty():
		stack.top().next = head
		head = stack.pop()
	return head


def remove_value2(head, num):
	"""删除指定值的节点的具体实现"""
	while head is not None:
		if head.value != num:
			break
		head = head.next
	pre = head
	cur = head
	while cur is not None:
		if cur.value == num:
			pre.next = cur.next
		else:
			pre = cur
		cur = cur.next
	return head
