# 基于分治法的快速排序算法
import random

from development.chapter12.merge_list import merge_sort
from development.chapter7.LinkedQueue import LinkedQueue


def quick_sort(S):
	"""对队列进行快速排序"""
	n = len(S)
	if n < 2: return
	p = S.first()
	L = LinkedQueue()
	E = LinkedQueue()
	G = LinkedQueue()
	while not S.is_empty():
		while S.first() < p:
			L.enqueue(S.dequeue())
		while S.first() == p:
			E.enqueue(S.dequeue())
		while S.first() > p:
			G.enqueue(S.dequeue())
	quick_sort(L)
	quick_sort(G)
	while not L.is_empty():
		S.enqueue(L.dequeue())
	while not E.is_empty():
		S.enqueue(E.dequeue())
	while not G.is_empty():
		S.enqueue(G.dequeue())


def inplace_quick_sort(S, a, b):
	"""对列表S进行快速排序"""
	if a > b: return
	pivot = S[b]
	left = a
	right = b - 1
	while left <= right:
		while left <= right and S[left] < pivot:
			left += 1
		while left <= right and S[right] > pivot:
			right -= 1
		if left <= right:
			S[left], S[right] = S[right], S[left]
			left, right = left + 1, right + 1
	S[left], pivot = pivot, S[left]
	inplace_quick_sort(S, a, left - 1)
	inplace_quick_sort(S, left + 1, b)


class _Item:  # ------------->用与装饰的类
	def __init__(self, k, v):
		self._key = k
		self._value = v


def decorated_merge_sort(data, key=None):
	"""装饰-->排序--->取消设计模式"""  # 主要思想是先加上装饰在用装饰好的排序 排序完成后在取消装饰
	if key is not None:
		for j in range(len(data)):
			# 每一个data都用_Item类来实例化
			data[j] = _Item(key(data[j]), data[j])  # --->加上装饰的过程
	merge_sort(data)  # ---------------------------->进行排序的过程
	if key is not None:
		for j in range(len(data)):
			data[j] = data[j]._value  # --------------->取消装饰的过程


def quick_select(S, k):
	"""随机快速选择"""
	if len(S) == 1:
		return S[0]
	pivot = random.choice(S)
	L = [x for x in S if x < pivot]
	E = [x for x in S if x == pivot]
	G = [x for x in S if x > pivot]
	if k < len(L):
		return quick_select(L, k)
	elif k <= len(L) + len(E):
		return pivot
	else:
		j = k - len(L) - len(E)
		return quick_select(G, j)
