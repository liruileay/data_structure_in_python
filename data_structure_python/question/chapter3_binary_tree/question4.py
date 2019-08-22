"""
如何较为直观的打印一颗二叉树
"""


class Node:
	
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None


node_list = [Node(i) for i in range(7)]
node_list[0].left = node_list[1]
node_list[0].right = node_list[2]
node_list[1].left = node_list[3]
node_list[3].right = node_list[6]
node_list[2].left = node_list[4]
node_list[2].right = node_list[5]

head = node_list[0]


def print_in_order(head, height: int, to, length):
	"""打印一颗二叉树的方法实现过程"""
	if head is None:
		return
	print(head, height + 1, "v", length)
	val = to + str(head.value) + to
	len_m = len(val)
	len_l = (length - len_m) // 2
	len_r = length - len_l - len_m
	val = str(len_l) + val + str(len_r)
	print(str(height * length) + val)
	print_in_order(head.left, height + 1, "^", length)


def print_tree(head):
	"""直观打印二叉树的方法"""
	print("Binary Tree:")
	print_in_order(head, 0, "H", 17)
	print("Over")


if __name__ == '__main__':
	print_tree(head)
