"""
一种怪异的节点删除方式
"""


class RemoveLastError(Exception):
	pass


def remove_node_wired(head):
	'''一种怪异的节点删除方式的具体实现'''
	if head is None:
		return
	next = head.next
	if next is None:
		raise RemoveLastError('can not remove the last error')
	head.value = next.value
	head.next = next.next
	
