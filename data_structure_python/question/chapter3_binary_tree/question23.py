"""
通过先序和中序数组生成后序数组
	题目；已知一颗二叉树所有节点值都不相同，给定这颗树正确的先序和中序数组，不要重建整颗树，而是通过这两个数组直接生成正确的后序数组。
"""
from development.chapter10.ChainHashMap import ChainHashMap


def set_pos(p, pi, pj, n, ni, nj, s, si, map):
	if pi > pj:
		return si
	s[si] = p[pi]
	si -= 1
	i = map.get(p[pi])
	si = set_pos(p, pj - nj + i + 1, pj, n, i + 1, nj, s, si, map)
	return set_pos(p, pi + 1, pi + i - ni, n, ni, i - 1, s, si, map)


def get_pos_array(pre, n):
	'''通过先序和中序生成后序数组的具体实现'''
	if pre is None or n is None:
		return None
	length = len(pre)
	pos = [None] * length
	map = ChainHashMap()
	for i in range(length):
		map[n[i]] = i
	set_pos(pre, 0, length - 1, n, 0, length - 1, pos, length - 1, map)
	return pos
