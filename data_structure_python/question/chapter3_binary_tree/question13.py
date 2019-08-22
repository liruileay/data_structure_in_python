"""
判断t1树种是否有与t2树拓扑结构完全相同的子树
	题目:
		给定彼此独立的两颗头节点分别为t1和t2,判断t1中是否有与t2树拓扑结构完全相同的子树
		
"""
from question.chapter3_binary_tree.question2 import serial_by_pre


def get_next_array(ms):
	'''kmp最大子串'''
	if len(ms) == 1:
		return [-1]
	next = [0] * len(ms)
	next[0] = -1
	next[1] = 0
	pos = 2
	cn = 0
	while pos < len(next):
		if ms[pos - 1] == ms[cn]:
			cn += 1
			next[pos] = cn
			pos += 1
		elif cn > 0:
			cn = next[cn]
		else:
			next[pos] = 0
			pos += 1
	return next


def get_index_of(s, m):
	'''kmp进行匹配看是否存在'''
	if s is None or m is None or len(m) < 1 or len(s) < len(m):
		return -1
	ss = list(s)
	ms = list(m)
	si = 0
	mi = 0
	next = get_next_array(ms)
	while si < len(ss) and mi < len(ms):
		if ss[si] == ms[mi]:
			si += 1
			mi += 1
		elif next[mi] == -1:
			si += 1
		else:
			mi = next[mi]
	return si - mi if mi == len(ms) else -1


def is_sub_tree(t1, t2):
	t1_str = serial_by_pre(t1)
	t2_str = serial_by_pre(t2)
	return get_index_of(t1_str, t2_str)
