# 4.1
import os


def RerurnMax(S):
	if len(S) == 1: return S[0]
	mid = len(S) // 2
	left_max = RerurnMax(S[:mid])
	right_max = RerurnMax(S[mid:])
	return left_max if left_max > right_max else right_max


print(RerurnMax([1, 2, 3, 4, 5, 6, 7]))


# 4.6调和级数

def ReturnNum(n):
	if n == 1: return 1
	return 1 / n + ReturnNum(n - 1)


print(ReturnNum(3))


# 4.12
def ReturnAbsNum(m, n):
	if m == 0: return 0
	if n == 0: return 0
	return m + ReturnAbsNum(m, n - 1)


print(ReturnAbsNum(5, 7))


# 4.15
def ReturnSonCollection(S):
	if S: print(S)
	if S == []: return
	return ReturnSonCollection(S[:len(S) - 1])


print(ReturnSonCollection([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


# 4.18
def AEIOUIsMany(String: str):  # 元音字母a e i o u
	"""元音字母多返回true否则为false"""
	
	def Count(String):
		if not String: return 0
		count = 1 if String[0] in ["a", "e", "i", "o", "u"] and String else 0
		return count + Count(String[1:])
	
	count = Count(String)
	if count > len(String) - count:
		return True
	return False


print(AEIOUIsMany("aeiousfsfwpwgknvaeae"))


def EvenBeforeOdd(list, start, stop):
	"""奇数在偶数的后面"""
	if start < stop:
		if list[start] % 2 == 1:
			list[start], list[stop - 1] = list[stop - 1], list[start]
			stop, start = stop - 1, start + 1
			EvenBeforeOdd(list, start, stop)
		else:
			stop, start = stop - 1, start + 1
			EvenBeforeOdd(list, start, stop)
	return list


print(EvenBeforeOdd([1, 2, 3, 4, 5, 6, 7, 8], 0, 8))


def InsertIn(list, target, start, stop):
	if start < stop:
		if list[start] <= target:
			start += 1
			InsertIn(list, target, start, stop)
		else:
			list[start], list[stop - 1] = list[stop - 1], list[start]
			stop -= 1
			InsertIn(list, target, start, stop)
	return list


print(InsertIn([9, 8, 7, 6, 5, 4, 3, 2, 1], 5, 0, 9))


def SumK(list, k, start):
	"""序列为升序任取两个数他们的总和为k输出那两个数"""
	if start >= len(list):
		return None
	if list[start] + list[len(list) - 1] < k:
		return None
	if list[start] > k:
		return None
	if k - list[start] in list:
		return list[start], k - list[start]
	else:
		start += 1
		SumK(list, k, start)


print(SumK([1, 2, 3, 4, 5, 6, 7, 8, 9], 6, 0))


def FindPath(path):
	total = os.path.getsize(path)
	if os.path.isdir(path):
		for filename in os.listdir(path):
			child = os.path.join(path, filename)
			total += FindPath(child)
	return total


"""
pot + pan = bib
dog + cat = pig
boy + girl = baby
"""
"""
"""


def FindNumForLetter(p, o, t, c, a, n, b, i, d, g, y, r, l):
	if (p * 100 + o * 10 + t) + (p * 100 + a * 10 + n) == \
			b * 100 + i * 10 + b and (d * 100 + o * 10 + g) \
			+ (c * 100 + a * 10 + t) == p * 100 + i * 10 + g \
			and (b * 100 + o * 10 + y) + (g * 1000 + i * 100
			                              + r * 10 + l) == b * 1000 + a * 100 + b * 10 + y:
		return p, o, t, c, a, n, b, i, d, g, y, r, l
	
