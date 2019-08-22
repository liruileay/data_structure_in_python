"""删除链表的中间的节点"""
import math


def remove_mid_node(head):
	"""删除链表中最中间的节点"""
	if head is None or head.next is None:
		return head
	if head.next.next is None:
		return head.next
	pre = head
	cur = head.next.next
	while cur.next is not None and cur.next.next is not None:
		pre = pre.next
		"""# 表示链表长度每次增加2中间节点就向后移动一位"""
		cur = cur.next.next
	pre.next = pre.next.next
	return head


def remove_by_ratio(head, a, b):
	"""删除在a/b处对应的节点"""
	if a < 1 or a > b:
		return head
	n = 0
	cur = head
	while cur is not None:
		n += 1
		cur = cur.next
	n = math.ceil((n * a) // b)
	if n == 1:
		head = head.next
	while n > 1:
		cur = head
		while n != 1:
			n -= 1
			cur = cur.next
		cur.next = cur.next.next
	return head
