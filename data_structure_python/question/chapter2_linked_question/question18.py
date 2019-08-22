"""向有序的环形单链表种插入新的值"""


class Node(object):
	def __init__(self, data):
		self.value = data
		self.next = None


def insert_num(head, num):
	"""向有序环形链表种插入新值的具体实现"""
	node = Node(num)
	if head is None:
		node.next = node
		return node
	pre = head
	cur = head.next
	while cur is not head:
		if pre.value <= num and cur.value >= num:
			break
		pre = cur
		cur = cur.next
	pre.next = node
	node.next = cur
	return head if head.value < num else node

