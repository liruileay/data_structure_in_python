"""
在二叉树中找到两个节点的最近公共祖先
题目: 给定一颗二叉树的头节点head,以及这棵树中的两个节点o1和o2,请返回o1和o2的最近公共祖先
	进阶:如果查询两个节点的最近公共祖先节点的操作十分繁琐,想法让单条查询的查询时间减少
	再进阶:给定二叉树的头节点head,同时给定所有想要进行的查询。二叉树的节点数量为N,查询条数为M,
		请在时间复杂度为O(N+M)内返回所有的查询结果
"""


def lowest_ancestor(head, o1, o2):
	'''找到二叉树的公共祖先节点'''
	if head is None or head is o1 or head is o2:
		return head
	left = lowest_ancestor(head.left, o1, o2)
	right = lowest_ancestor(head.right, o1, o2)
	if left is not None and right is not None:
		return head
	return left if left is not None else right

