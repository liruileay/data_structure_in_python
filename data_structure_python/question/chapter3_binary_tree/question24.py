"""
统计生成所有不同的二叉树
	题目: 给定一个整数N，如果N<1,代表空树结构,否则代表中序遍历的结果为{1，2，3.。。N}
	请返回可能的二叉树结构由多少。
	例如，N = -1时，代表空树结构，返回1；N=2时，满足中序遍历为{1，2}的二叉树结构只有图3-49所示的两种
		所以返回结果为2.
	进阶：N的含义不变，假设可能的二叉树结构由M种，请返回M个二叉树的头节点，每一颗二叉树代表一种可能的结构
"""
from question.chapter1_stack_queue_question.question9 import Node


def num_tree(n):
	if n < 2:
		return 1
	num = [0] * (n + 1)
	num[0] = 1
	for i in range(n + 1):
		for j in range(i + 1):
			num[i] += num[j - 1] + num[i - j]
	return num[n]


