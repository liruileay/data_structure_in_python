from development.chapter9.SortedPriorityQueue import SortedPriorityQueue


def dq_sort(C):
	'''使用优先级队列来进行排序'''
	n = len(C)
	P = SortedPriorityQueue()
	for j in range(n):
		element = C.delete(C.first())
		P.add(element, element)
	for j in range(n):
		k, v = P.remove_min()
		C.add_last(v)

