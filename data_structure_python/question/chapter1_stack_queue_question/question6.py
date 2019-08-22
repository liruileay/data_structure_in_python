"""用栈实现解决汉诺塔问题"""

"""
汉诺塔问题进阶:
	现在限制不能从最左侧的塔直接移动到最右,也不能从最右移动到最左,必须要经过中间的
	求一个N层的汉诺塔问题的求解,打印最优移动过程和最优的步数
	

"""


def process(num, left, mid, right, fro, to):
	"""打印汉诺塔的具体实现过程"""
	if num == 1:  # 表示1层的时候的汉诺塔问题
		if fro == mid or to == mid:
			print("Move 1 from {} to {}".format(fro, to))
			return 1
		else:
			print("Move 1 from {} to {}".format(fro, mid))
			print("Move 1 from {} to {}".format(mid, to))
			return 2
	if fro == mid or to == mid:
		another = right if fro == left or to == left else left
		part1 = process(num - 1, left, mid, right, fro, another)
		part2 = 1
		print("Move {} from {} to {}".format(num, fro, to))
		part3 = process(num - 1, left, mid, right, another, to)
		return part1 + part2 + part3
	else:
		part1 = process(num - 1, left, mid, right, fro, to)
		part2 = 1
		print("Move {} from {} to {}".format(num, fro, mid))
		part3 = process(num - 1, left, mid, right, to, fro)
		part4 = 1
		print("Move {} from {} to {}".format(num, mid, to))
		part5 = process(num - 1, left, mid, right, fro, to)
		return part1 + part2 + part3 + part4 + part5


def hanoi_problem1(num, left, mid, right):
	"""汉诺塔问题解决"""
	if num < 1:
		return 0
	return process(num, left, mid, right, left, right)


if __name__ == '__main__':
	hanoi_problem1(5, "left", "mid", "right")
