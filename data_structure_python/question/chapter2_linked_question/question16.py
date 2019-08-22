"""单链表的选择排序
	题目: 给定一个无序单链表的头节点head,实现单链表的选择排序
	要求:额外空间为O(1)
"""


class Node(object):
	def __init__(self, data):
		self.value = data
		self.next = None


def get_small_est_pre_node(head):
	small_pre = None
	small = head
	pre = head
	cur = head.next
	while cur is not None:
		if cur.value < small.value:
			small_pre = pre
			small = cur
		pre = cur
		cur = cur.next
	return small_pre



def selection_sort(head):
	"""链表的选择排序具体实现"""
	tail = None
	cur = head
	while cur is not None:
		small = cur
		small_pre = get_small_est_pre_node(cur)
		if small_pre is not None:
			small = small_pre.next
			small_pre.next = small.next
		cur = cur.next if cur is small else cur
		if tail is None:
			head = small
		else:
			tail.next = small
		tail = small
	return head
