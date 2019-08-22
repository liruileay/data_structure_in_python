RESULT = 0


def Merge(list, left, mid, right):
	"""将两个子数组进行归并排序"""
	left_list, right_list, result, l_cur, r_cur = list[left:mid], list[mid:right], [], 0, 0
	while l_cur < len(left_list) and r_cur < len(right_list):
		if left_list[l_cur] <= right_list[r_cur]:
			global RESULT
			RESULT += left_list[l_cur] * (len(right_list)-r_cur)
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
