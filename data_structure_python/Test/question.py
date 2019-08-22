def get_all_way(k, N, arr):
	'''
	
	:param k: 表示小球种类
	:param N: 表示挑选小球的个数
	:param arr: 表示每一个种类对应的个数
	:return:
	'''
	total = 0
	for i in arr:
		total += i
	if total < N:
		return
	type_arr = []
	type_a = [[0] * k]
	for i in range(k):
		pass
