"""
题目:给定整数N，返回斐波那契数列的第N项
	补充题目1:
		给定整数N，代表台阶数，一次可以跨2个或者1个台阶，返回还有多少种走法。
	
	补充题目2:
		假设农场中成熟的母牛每年只会生1头小母牛,并且永远不会死。第一年农场有1只成熟的母牛,从第二年开始,母牛开始生小牛
		。每只小母牛3年之后成熟又可以生小母牛。给定整数N,求出N年后牛的数量。
"""


def f1(n):
	if n < 1:
		return 0
	if n == 1 or n == 2:
		return 1
	return f1(n - 1) + f1(n - 2)


def f2(n):
	if n < 1:
		return 0
	if n == 1 or n == 2:
		return 1
	res = 1
	pre = 1
	for i in range(3, n):
		temp = res
		res += pre
		pre = temp
	return res



	
