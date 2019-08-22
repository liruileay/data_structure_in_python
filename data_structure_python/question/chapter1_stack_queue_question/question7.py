"""同汉诺塔问题用非递归方法实现"""
from development.chapter6.ArrayStack import ArrayStack


def hanoi_problem2(num, left, mid, right):
	lS = ArrayStack()
	mS = ArrayStack()
	rS = ArrayStack()
	
