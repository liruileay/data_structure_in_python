# 基于分治法的链表归并排序的python实现
from development.chapter7.LinkedQueue import LinkedQueue


def merge(S1, S2, S):
	"""将两个队列S1和S2归并到空的队列S中"""
	while not S1.is_empty() and not S2.is_empty():
		if S1.first() < S2.first():
			S.enqueue(S1.dequeue())
		else:
			S.enqueue(S2.dequeue())
	while not S1.is_empty():
		S.enqueue(S1.dequeue())
	while not S2.is_empty():
		S.enqueue(S2.dequeue())


def merge_sort(S):
	"""对队列S进行归并排序"""
	n = len(S)
	if len(S) < 2:
		return
	S1 = LinkedQueue()
	S2 = LinkedQueue()
	while len(S1) < n // 2:
		S1.enqueue(S.dequeue())
	while not S.is_empty():
		S2.enqueue(S.dequeue())
	merge_sort(S1)
	merge_sort(S2)
	merge(S1, S2, S)
