"""图的广度优先搜索"""
import copy
import random


def BFS(g, s, discovered):
	"""图的广度优先搜索"""
	level = [s]
	while len(level) > 0:
		next_level = []
		for u in level:
			for e in g.incident_edges(u):
				v = e.opposite(u)
				if v not in discovered:
					discovered[v] = e
					next_level.append(v)
		level = next_level


def BFS_complate(g):
	"""返回全部图的广度优先搜索"""
	forest = {}
	for u in g.vertices():
		if u not in forest:
			forest[u] = None
			BFS(g, u, forest)
	return forest


def insertheapify(L: list, index):
	"""将一个数组初始化成为一个小根堆"""
	while L[index] < L[(index - 1) // 2] and (index - 1) // 2 >= 0:
		L[index], L[(index - 1) // 2] = L[(index - 1) // 2], L[index]
		index = (index - 1) // 2


def heapify(L: list, index, size):
	"""取出元素后将原来的数组还原成为一个小根堆"""
	left = 2 * index + 1
	while left < size:
		minest = left + 1 if left + 1 < size and L[left + 1] < L[left] else left
		if minest == index: break
		L[index], L[minest] = L[minest], L[index]
		index, left = minest, 2 * minest + 1
	print(L)


def get_min(L):
	L[0], L[len(L) - 1] = L[len(L) - 1], L[0]
	return L.pop()


def get_min_sum(L: list, R: list) -> int:
	"""输入两个数组任意交换得到两个数组的差值最小值"""
	sum = 0
	L.extend(R)
	for i in range(1, len(L)):
		"""初始化一个小根堆"""
		insertheapify(L, i)
	while L:
		min1 = get_min(L)  # 弹出一个最小的数
		heapify(L, 0, len(L))
		min2 = get_min(L)  # 弹出一个最小的数
		heapify(L, 0, len(L))
		sum += abs(min1 - min2)
	return sum


if __name__ == '__main__':
	L = [random.randint(0, 10) for i in range(11)]
	R = [random.randint(0, 10) for i in range(11)]
	a = copy.deepcopy(L)
	b = copy.deepcopy(R)
	a.extend(b)
	a.sort(reverse=True)
	min_sum = 0
	while a:
		c = a.pop()
		min_sum += abs(c - a.pop())
	sum = get_min_sum(L, R)
	if sum == min_sum:
		print("Success")
	else:
		print("Failure")
