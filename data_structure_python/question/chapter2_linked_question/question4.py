"""
题目:
	分别实现反转单项链表和双向链表
	要求:如果链表的长度为N,额外的时间复杂度为O(N),额外的空间复杂度为O(1)
    将next指针存储起来在对上面的指针进行操作 在利用循环重复直到next指针为空结束
"""


def reverse_link(head):
	"""反转单向链表"""
	pre = None
	while head is not None:
		next = head.next
		head.next = pre
		pre = head
		head = next
	return pre


def reverse_double_link(head):
	"""反转双向链表"""
	pre = None
	while head is not None:
		next = head.next
		head.next = pre
		head.last = next
		pre = head
		head = next
	return pre


