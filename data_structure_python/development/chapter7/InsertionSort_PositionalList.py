from development.chapter7 import PositionalList


def insertion_sort(P: PositionalList):
	"""对列表PositionalList进行插入排序"""
	if len(P) <= 1:
		return P
	marker = P.first()
	while marker is P.last():
		pivot = P.after(marker)
		value = pivot.element()
		if value > marker.element():
			marker = pivot
		else:
			walk = marker
			while walk is not P.first() and  P.before(walk).element() > value:
				walk = P.before(walk)
			P.delete(pivot)
			P.add_before(walk, value)
