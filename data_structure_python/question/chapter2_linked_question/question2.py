"""
题目:
  分别实现两个函数,一个可以删除单链表中倒数第k个节点,另一个可以删除双链表中倒数第k个节点
  要求:
    如果链表长度为N要求时间复杂度达到O(N),额外空间空间复杂度达到O(1)
    
"""


def remove_last_Kth_node(head, k):
	"""移出单链表的倒数第k个节点"""
	if head is None or k < 1:
		return head
	cur = head
	while cur is not None:
		k -= 1
		cur = cur.next
	if k == 0:
		head = head.next
	if k < 0:
		cur = head
		while k != 0:
			k += 1
		cur.next = cur.next.next
	return head


def remove_last_double_Kth_node(head, k):
	"""移出双链表的倒数第k个节点"""
	if head is None or k < 1:
		return head
	cur = head
	while cur is not None:
		k -= 1
		cur = cur.next
	if k == 0:
		head = head.next
		head.last = None
	if k < 0:
		cur = head
		while k != 0:
			k += 1
			cur = cur.next
		new_next = cur.next.next
		cur.next = new_next
		if new_next is not None:
			new_next.last = cur
	return head

