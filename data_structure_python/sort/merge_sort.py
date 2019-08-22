import copy
import random


def merge(left, right):
	"""将两个有序的子数组进行归并"""
	left_cur, right_cur, result = 0, 0, []
	while left_cur < len(left) and right_cur < len(right):
		if left[left_cur] < right[right_cur]:
			result.append(left[left_cur])
			left_cur += 1
		else:
			result.append(right[right_cur])
			right_cur += 1
	result += left[left_cur:] if left[left_cur:] else right[right_cur:]
	return result


def MergeSort_resursion(list):
	"""插入排序的递归实现"""
	if len(list) == 1:
		return list
	left, right = MergeSort_resursion(list[:(len(list) // 2)]), MergeSort_resursion(list[(len(list) // 2):])
	result = merge(left, right)
	return result


def Merge(list, left, mid, right):
	"""将两个子数组进行归并排序"""
	left_list, right_list, result, l_cur, r_cur = list[left:mid], list[mid:right], [], 0, 0
	while l_cur < len(left_list) and r_cur < len(right_list):
		if left_list[l_cur] <= right_list[r_cur]:
			result.append(left_list[l_cur])
			l_cur += 1
		else:
			result.append(right_list[r_cur])
			r_cur += 1
	result += left_list[l_cur:] if left_list[l_cur:] else right_list[r_cur:]
	list[left:right] = result


def MergeSort(list):
	"""归并排序的非递归实现"""
	size = 1
	while size < len(list):
		left = 0
		while left < len(list):
			mid = left + size
			right = min(mid + size, len(list))
			Merge(list, left, mid, right)
			left = mid + size
		size = 2 * size
	return list


def main():
	list = [random.randint(0, 100) for i in range(1000)]
	list1 = MergeSort_resursion(copy.deepcopy(list))
	item = sorted(copy.deepcopy(list))
	list = MergeSort(list)
	for i in range(len(list)):
		if list[i] == item[i] == list1[i]:
			continue
		else:
			raise ValueError("Failure")
	print("Success")


if __name__ == '__main__':
	main()
