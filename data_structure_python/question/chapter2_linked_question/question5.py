"""反转部分单向链表"""


def reserve_part(head, fro: int, to: int):
	"""反转部分链表从fro到to的部分链表部分"""
	len = 0
	node1 = head
	fPre = None
	tPos = None
	while node1 is not None:
		len += 1
		fPre = node1 if len == fro - 1 else fPre
		tPos = node1 if len == to + 1 else tPos
		node1 = node1.next
	if fro > to or fro < 1 or to > len:
		return head
	node1 = head if fPre is None else fPre.next
	node2 = node1.next
	node1.next = tPos
	while node2 is not tPos:
		next = node2.next
		node2.next = node1
		node1 = node2
		node2 = next
	if fPre is not None:
		fPre.next = node1
		return head
	return node1
