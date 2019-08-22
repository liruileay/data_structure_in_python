import copy
import random


def BucketSort(list: list) -> list:
	"""桶排序或者计数排序时间复杂度取决与桶的大小"""
	if len(list) <= 1:
		return list
	min, largest = list[0], list[0]
	for j in list:
		min, largest = list[j] if list[j] < min else min, list[j] if list[j] > largest else largest
	bucket, result = [0] * (largest - min + 1), []
	for k in list:
		bucket[k - min] += 1
	for i in range(len(bucket)):
		if bucket[i] > 0:
			for j in range(bucket[i]):
				result.append(min + i)
	return result


def main():
	list = [random.randint(0, 100) for i in range(1000)]
	item = sorted(copy.deepcopy(list))
	list = BucketSort(list)
	for i in range(len(list)):
		if list[i] == item[i]:
			continue
		else:
			raise ValueError("Failure")
	print("Success")


if __name__ == '__main__':
	main()
