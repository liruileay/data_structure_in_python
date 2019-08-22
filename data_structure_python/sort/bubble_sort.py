import copy
import random


def BubbleSort(list):
	"""实现冒泡排序把最大的放在最后面"""
	for k in range(len(list)-1,0,-1):
		for j in range(0,k):
			if list[j]>list[j+1]:
				list[j],list[j+1] = list[j+1],list[j]
	return list

def main():
	list = [random.randint(0,100) for i in range(1000)]
	item = sorted(copy.deepcopy(list))
	list = BubbleSort(list)
	for i in range(len(list)):
		if list[i] == item[i]:
			continue
		else:
			raise ValueError("Failure")
	print("Success")


if __name__ == '__main__':
	main()