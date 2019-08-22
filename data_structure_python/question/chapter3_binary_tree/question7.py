"""在二叉树中找到累加值为指定值的最长子数组长度"""
from development.chapter10.ChainHashMap import ChainHashMap


def pre_order(head, sum, pre_sum, level, max_len, hash_map):
	"""返回累加和为指定值的最长路径长度的具体实现"""
	if head is None:
		return max_len
	cur_sum = pre_sum + head.value
	if not hash_map.__contains__(cur_sum):
		hash_map[cur_sum] = level
	if hash_map.__contains__(cur_sum - sum):
		max_len = max(level - hash_map[cur_sum - sum], max_len)
	max_len = pre_order(head.left, sum, cur_sum, level + 1, max_len, hash_map)
	max_len = pre_order(head.right, sum, cur_sum, level + 1, max_len, hash_map)
	if level == hash_map(cur_sum):
		hash_map.pop(cur_sum)
	return max_len


def get_max_length(head, sum):
	'''累加和为指定值的最长路径长度'''
	sum_map = ChainHashMap()
	sum_map[0] = 0
	return pre_order(head, sum, 0, 1, 0, sum_map)


def get_max_arr_length(arr, k):
	"""得到arr的子数组中数组元素相加为k的最长子数组"""
	if arr is None or len(arr) == 0 or k <= 0:
		return 0
	left, right, length, sum = 0, 0, 0, arr[0]
	while right < len(arr):
		if sum == k:
			length = max(length, right - left + 1)
			sum -= arr[left]
			left += 1
		elif sum < k:
			right += 1
			if right == len(arr):
				break
			sum += arr[right]
		else:
			sum -= arr[left]
			left += 1
	return length


print(get_max_arr_length([1, 2, 3, 4, 1, 1, 5, 2, 1, 1], 7))
