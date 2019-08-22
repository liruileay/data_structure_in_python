"""合并两个有序的单链表"""


def merge_node(head1, head2):
	"""合并两个有序的单链表的具体实现"""
	if head1 is None or head2 is None:
		return head1 if head2 is None else head2
	head = head1 if head1.value < head2.value else head2
	cur1 = head1 if head is head1 else head2
	cur2 = head2 if head is head2 else head1
	pre = None
	while cur1 is not None and cur2 is not None:
		if cur1.value <= cur2.value:
			pre = cur1
			cur1 = cur1.next
		else:
			next = cur2.next
			pre.next = cur2
			cur2.next = next
			pre = cur2
			cur2 = next
	pre.next = cur2 if cur1 is None else cur1
	return head
	