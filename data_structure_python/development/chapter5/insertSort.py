import copy
import random


def insertSort(list):
	'''插入排序算法'''
	for k in range(1, len(list)):
		for j in range(k, 0, -1):
			if list[j - 1] > list[j]:
				list[j], list[j - 1] = list[j - 1], list[j]
	return list


def insertion_sort(list):
	'''插入排序算法'''
	for k in range(len(list)):
		cur = list[k]
		j = k
		while j > 0 and list[j - 1] > cur:
			list[j] = list[j - 1]
			list[j - 1] = cur
			j -= 1
	return list


if __name__ == '__main__':
	list = [random.randint(0, 10000) for i in range(1000)]
	temp = sorted(copy.deepcopy(list))
	item = insertion_sort(copy.deepcopy(list))
	list = insertSort(list)
	for k in range(1000):
		if temp[k] == list[k] == item[k]:
			continue
		print("failure")
	print("Success")
