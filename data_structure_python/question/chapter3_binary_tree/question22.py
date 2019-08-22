"""
先序,中序,后序数组两两结合重构二叉树
	题目:
		已知一颗二叉树的所有节点值都是不相同,给定这颗树二叉树正确的先序,中序,后序数组。
		请分别用三个函数实现任意连个数组结合重构原来的二叉树,并返回重构二叉树的头节点
		
"""
from development.chapter10.ChainHashMap import ChainHashMap
from question.chapter1_stack_queue_question.question9 import Node


def pre_in(p, pi, pj, n, ni, nj, hash_map):
	"""先序和中序重构过程"""
	if pi > pj:
		return None
	head = Node(p[pi])
	index = hash_map.get(p[pi])
	head.left = pre_in(p, pi + 1, pi + index - ni, n, ni, index - 1, hash_map)
	head.right = pre_in(p, pi + index - ni + 1, pj, n, index + 1, nj, hash_map)
	return head


def pre_in_to_tree(pre, n):
	"""先序和中序结合重构二叉树"""
	if pre is None or n is None:
		return None
	hash_map = ChainHashMap()
	for i in range(len(n)):
		hash_map[n[i]] = i
	return pre_in(pre, 0, len(pre) - 1, n, 0, len(n) - 1, hash_map)


def in_pos(n, ni, nj, s, si, sj, hash_map):
	if si > sj:
		return None
	head = Node(s[sj])
	index = hash_map.get(s[sj])
	head.left = in_pos(n, ni, index - 1, s, si, si + index - ni - 1, hash_map)
	head.right = in_pos(n, index + 1, nj, s, si + index - ni, sj - 1, hash_map)
	return head


def in_pos_to_tree(n, pos):
	if n is None or pos is None:
		return None
	hash_map = ChainHashMap()
	for i in range(len(n)):
		hash_map[n[i]] = i
	return in_pos(n, 0, len(n) - 1, pos, 0, len(pos) - 1, hash_map)


def pre_pos(p, pi, pj, s, si, sj, hash_map):
	head = Node(s[sj])
	sj -= 1
	if pi is pj:
		return head
	pi += 1
	index = hash_map.get(p[pi])
	head.left = pre_pos(p, pi, pi + index - si, s, si, index, hash_map)
	head.right = pre_pos(p, pi + index - si + 1, pj, s, index + 1, sj, hash_map)
	return head


def pre_pos_to_tree(pre, pos):
	if pre is None or pos is None:
		return None
	hash_map = ChainHashMap()
	for i in range(len(pos)):
		hash_map[pos[i]] = i
	return pre_pos(pre, 0, len(pre) - 1, pos, 0, len(pos) - 1, hash_map)
