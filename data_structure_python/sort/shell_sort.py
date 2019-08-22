import copy
import random


def ShellSort(list):
	"""希尔排序(插入排序的一种)"""
	size, gap = len(list), len(list) // 2
	while gap > 0:
		for k in range(gap, size):
			while k > 0:
				if list[k] < list[k - gap]:
					list[k], list[k - gap] = list[k - gap], list[k]
				k -= gap
		gap = gap // 2

def main():
	list = [random.randint(-10000, 10000) for i in range(100)]
	list2 = sorted(copy.deepcopy(list))
	ShellSort(list)
	error = []
	i = 0
	while i < 100:
		if list[i] == list2[i]:
			i += 1
			continue
		else:
			error.append(i)
		i += 1
	if not error:
		print("Success")
	else:
		print(error)


if __name__ == '__main__':
	main()