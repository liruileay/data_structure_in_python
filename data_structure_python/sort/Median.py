import random


def heapify_max(list, index, size):
	"""将列表调整成为大根堆"""
	left = index * 2 + 1
	while left < size:
		largest = left + 1 if left + 1 < size and list[left] < list[left + 1] else left
		largest = index if list[largest] < list[index] else largest
		if largest == index:
			break
		list[index], list[largest] = list[largest], list[index]
		index, left = largest, largest * 2 + 1


def heapify_min(list, index, size):
	"""将列表调整成位小根堆"""
	left = index * 2 + 1
	while left < size:
		min = left + 1 if left + 1 < size and list[left + 1] < list[left] else left
		min = index if list[index] < list[min] else min
		if min == index:
			break
		list[min], list[index] = list[index], list[min]
		index, left = min, index * 2 + 1


def Median(list):
	"""小于的放在大根堆大的一半放在小根堆中位数等于列表长度长的的第一个元素"""
	index, largest_list, size, min_list = 1, [], len(list), []
	largest_list.append(list[0])
	while index < size:
		if abs(len(largest_list) - len(min_list)) == 2:
			if len(largest_list) - len(min_list) == 2:
				min_list.insert(0, largest_list[0])
				largest_list.pop(0)
			elif len(min_list) - len(largest_list) == 2:
				largest_list.insert(0, min_list[0])
				min_list.pop(0)
			heapify_max(largest_list, 0, len(largest_list))
			heapify_min(min_list, 0, len(min_list))
			continue
		if list[index] <= largest_list[0]:
			largest_list.insert(0, list[index])
			heapify_max(largest_list, 0, len(largest_list))
		elif list[index] > largest_list[0]:
			min_list.insert(0, list[index])
			heapify_min(min_list, 0, len(min_list))
		index += 1
	mid = largest_list[0] if len(largest_list) > len(min_list) else min_list[0]
	return largest_list, min_list, "mid={}".format(mid)


if __name__ == '__main__':
	list = [random.randint(0, 50) for i in range(40)]
	median = Median(list)
	print(median)
