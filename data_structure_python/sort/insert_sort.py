import copy
import random


def InsertSort(list):
	"""插入排序"""
	for k in range(1, len(list)):
		for j in range(k, 0, -1):
			if list[j - 1] > list[j]:
				list[j - 1], list[j] = list[j], list[j - 1]
	return list


def main():
	list = [random.randint(0,100) for i in range(1000)]
	item = sorted(copy.deepcopy(list))
	list = InsertSort(list)
	for i in range(len(list)):
		if list[i] == item[i]:
			continue
		else:
			raise ValueError("Failure")
	print("Success")


if __name__ == '__main__':
	main()
