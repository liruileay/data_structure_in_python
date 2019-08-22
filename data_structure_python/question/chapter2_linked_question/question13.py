"""删除无序单链表中重复出现的值
	方法一:使用哈希表
	方法二:选择排序的过程
"""


def remove_rep1(head):
	'''删除重复出现的值的节'''
	if head is None:
		return
	set_default = set()
	pre = head
	cur = head.next
	set_default.add(head.value)
	while cur is not None:
		if set_default.__contains__(cur.value):
			pre.next = cur.next
		else:
			set_default.add(cur.value)
			pre = cur
		cur = cur.next


def remove_rep2(head):
	'''删除重复出现的值的节点的进阶实现'''
	cur = head
	while cur is not None:
		pre = cur
		next = cur.next
		while next is not None:
			if cur.value == next.value:
				pre.next = next.next
			else:
				pre = next
			next = next.next
		cur = cur.next
