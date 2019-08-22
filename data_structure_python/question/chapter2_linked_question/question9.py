"""
复制含有随机指针的链表
"""

from development.chapter10.ChainHashMap import ChainHashMap


class Node(object):
	"""有随机节点的链表"""
	
	def __init__(self, data):
		self.value = data
		self.next = None
		self.rand = None


def copy_list_with_rand1(head):
	"""复制含有随机指针的链表的具体实现 会使用额外的空间哈希表"""
	map = ChainHashMap()
	cur = head
	while cur is not None:
		map.__setitem__(cur, Node(cur.value))
		cur = cur.next
	cur = head
	while cur is not None:
		map.get(cur).next = map.get(cur.next)
		map.get(cur).rand = map.get(cur.rand)
		cur = cur.next
	return map.get(head)


def copy_list_with_rand2(head):
	"""复制含有随机指针的链表的具体实现 不使用额外的空间"""
	if head is None:
		return None
	cur = head
	while cur is not None:
		next = cur.next
		cur.next = Node(cur.value)
		cur.next.next = next
		cur = cur.next
	cur = head
	while cur is not None:
		next = cur.next.next
		cur_copy = cur.next
		cur_copy.rand = cur.rand.next if cur.rand is not None else None
		cur = next
	res = head.next
	cur = head
	while cur is not None:
		next = cur.next.next
		cur_copy = cur.next
		cur.next = next
		cur_copy.next = cur_copy if cur_copy is not None else None
		cur = next
	return res
