# coding = utf-8
"""
10进制与2进制 互转

a >>n 相当与 a//2^n 指的是二进制往后移动n为
a <<n 相当于 a*2^n 指的是二进制向前移动n位
"""


def conver(n):
	"""
	10进制转2进制
	"""
	if n == 0:
		return 0
	temp = []
	while n:
		temp.append(n % 2)
		n = n >> 1
	temp.reverse()
	return "".join([str(x) for x in temp])


def reconver(str1):
	"""
	2进制转10进制
	"""
	temp = [int(x) for x in list(str1)]
	temp.reverse()
	sum = 0
	for i in range(0, len(temp)):
		sum += (1 << i) * temp[i]
	return sum


"""
移位运算 
>>1 右移1位，相当于 整数//2    
<<1 左移1位，相当于 整数*2
"""

print(reconver("1000"))
