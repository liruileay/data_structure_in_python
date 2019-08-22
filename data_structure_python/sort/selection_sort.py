import copy
import random


def SelectionSort(list):
	"""插入排序适合小样本的排序算法"""
	for k in range(len(list)):
		for j in range(k+1,len(list)):
			if list[k] >list[j]:
				list[k],list[j] = list[j],list[k]
	return list

def main():
	list = [random.randint(0,100) for i in range(1000)]
	item = sorted(copy.deepcopy(list))
	list = SelectionSort(list)
	for i in range(len(list)):
		if list[i] == item[i]:
			continue
		else:
			raise ValueError("Failure")
	print("Success")

#
if __name__ == '__main__':
	main()
