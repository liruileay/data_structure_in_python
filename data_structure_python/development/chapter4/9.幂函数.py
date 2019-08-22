def power(x, n):
	"""计算x的n次方"""
	if n == 0:
		return 1
	return x * power(x, n - 1)


def good_power(x, n):
	"""计算x的n次方"""
	if n == 0:
		return 1
	else:
		partial = good_power(x, n // 2)
		result = partial * partial
		if n % 2 == 1:  # 奇数多乘一个x
			result *= x
	return result
