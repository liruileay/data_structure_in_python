"""按照左右半区的方式重新组合单链表"""


def merge_LR(left, right):
	"""将左右merge在一起"""
	while left.next is not None:
		next = right.next
		right.next = left.next
		left.next = right
		left = right.next
		right = next
	left.next = right


def relocate(head):
	"""按照左右半区方式重连的具体实现"""
	if head is None or head.next is None:
		return
	mid = head
	right = head.next
	while right.next is not None and right.next.next is not None:
		mid = mid.next
		right = right.next.next
	right = mid.next
	mid.next = None
	merge_LR(head, right)
