import random


def netherlands(list, L, R, item):
	"""将小于mun的放在左边大于mun的放在右边"""
	left, right, cur = L - 1, R + 1, L
	while cur < right:
		if list[cur] < item:
			list[cur], list[left + 1], cur, left = list[left + 1], list[cur], cur + 1, left + 1
		elif list[cur] > item:
			list[cur], list[right - 1], right = list[right - 1], list[cur], right - 1
		elif list[cur] == item:
			cur += 1
	return list, f'item={item}  index{[left + 1, right - 1]}'


if __name__ == '__main__':
	list = [random.randint(0, 40) for i in range(20)]
	print(list)
	print(netherlands(list, 0, len(list) - 1, random.randint(0, 40)))
