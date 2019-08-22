import copy
import random


def heap_insert(list, index):
	"""通过找父节点将原始数组初始化为一个大根堆"""
	while list[(index - 1) // 2] < list[index] and (index - 1) // 2 >= 0:
		list[(index - 1) // 2], list[index] = list[index], list[(index - 1) // 2]
		index = (index - 1) // 2


def heapify(list, index, size):
	"""通过调整子节点的位置位重新变成大根堆"""
	left = index * 2 + 1
	while left < size:
		largest = left + 1 if list[left + 1] > list[left] and left + 1 < size else left
		largest = index if list[index] > list[largest] else largest
		if largest == index:
			break
		list[largest], list[index] = list[index], list[largest]
		index, left = largest, largest * 2 + 1


def Sort(list):
	"""堆排序"""
	for j in range(len(list)):
		heap_insert(list, j)
	list[0], list[len(list) - 1], size = list[len(list) - 1], list[0], len(list) - 1
	while size:
		heapify(list, 0, size)
		list[0], list[size - 1], size = list[size - 1], list[0], size - 1
	return list


def main():
	list = [random.randint(0, 100) for i in range(1000)]
	item = sorted(copy.deepcopy(list))
	list = Sort(list)
	for i in range(len(list)):
		if list[i] == item[i]:
			continue
		else:
			raise ValueError("Failure")
	print("Success")


if __name__ == '__main__':
	main()
