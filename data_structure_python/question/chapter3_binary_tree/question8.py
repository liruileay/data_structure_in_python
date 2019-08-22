"""找到二叉树中的搜索二叉树
	题目: 给定一颗树的头节点head,已知其中所有节点的值都不一样,找到含有节点最多的搜索二叉子树,
		并返回这个树的头节点
"""


def pos_order(head, record):
	'''返回二叉子树的头节点的具体实现'''
	if head is None:
		record[0] = 0
		record[1] = 0
		record[2] = 0
		return None
	value = head.value
	left = head.left
	right = head.right
	lBST = pos_order(left, record)
	lSize = record[0]
	lMin = record[1]
	lMax = record[2]
	rBST = pos_order(right, record)
	rSize = record[0]
	rMin = record[1]
	rMax = record[2]
	record[1] = min(lMin, value)
	record[2] = max(rMax, value)
	if left is lBST and right is rBST and lMax < value and value < rMin:
		record[0] = lSize + rSize + 1
		return head
	record[0] = max(rSize, lSize)
	return lBST if lSize > rSize else rBST


def biggest_sub_BST(head):
	'''返回二叉子树的头节点'''
	record = [None] * 3
	return pos_order(head, record)
