"""
题目:
定义二叉树的节点如下:
class Node:
	定义的MaxTree中每一个节点
	def __init__(self,element)
		self.element = element
		self.left = None
		self.right = None
一个数组的MaxTree定义如下
1.数组必须没有重复的元素
2.MaxTree是一个二叉树，数组的每一个值对应二叉树的一个节点
3.包括MaxTree树在其中的每一个子树,值的最大节点都是这个树的头节点
	给定一个没有重复元素的数组arr,写出生成这个数组的MaxTree的函数,
要求如果数组的长度为N,时间复杂度为O(N),额外空间复杂度为O(N)
"""
"""
题目解题方法
用一下原则建立这棵树:
	1.每一个数的父节点是他左边第一个比他大的数和右边第一个比它大的数中,较小的那个
	2.如果一个数左边是没有比他大的数，右边也没有。也就是说,这个数是整个数组的最大值,那么这个数是MaxTree的头节点
	3,4,5,1,2
			5
		  /   \
		 4     2
		/      /
	   3      1
	

"""
from development.chapter10.ChainHashMap import ChainHashMap
from development.chapter6.ArrayStack import ArrayStack


class Node:
	"""定义的MaxTree中每一个节点"""
	
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None


def pop_stack_set_map(stack, lBigMap):
	"""将节点设置在哈希表中"""
	popNode = stack.pop()
	if stack.is_empty():
		lBigMap.set(popNode, None)
	else:
		lBigMap.set(popNode, stack.top())


def get_max_tree(arr):
	"""用数组生成一个MaxTree树的具体实现"""
	nArr = [Node(i) for i in arr]
	stack = ArrayStack()
	lBigMap = ChainHashMap()
	rBigMap = ChainHashMap()
	for i in range(len(nArr)):
		curNode = nArr[i]
		# 栈中的元素要保持递减
		while (not stack.is_empty()) and stack.top().value < curNode.value:
			pop_stack_set_map(stack, lBigMap)  # 表示栈中的元素不是递减的时候执行的逻辑
		stack.push(curNode)
	while not stack.is_empty():  # 从栈中弹出元素
		pop_stack_set_map(stack, lBigMap)
	for i in range(len(nArr) - 1, -1, -1):
		curNode = nArr[i]
		while (not stack.is_empty()) and stack.top().value < curNode.value:
			pop_stack_set_map(stack, rBigMap)
		stack.push(curNode)
	while not stack.is_empty():
		pop_stack_set_map(stack, rBigMap)
	head = None
	for i in range(len(nArr)):
		curNode = nArr[i]
		left = lBigMap.get(curNode)
		right = rBigMap.get(curNode)
		if left is None and right is None:
			head = curNode
		elif left is None:
			if right.left is None:
				right.left = curNode
			else:
				right.right = curNode
		else:
			parent = left if left.value < right.value else right
			if parent.left is None:
				parent.left = curNode
			else:
				parent.right = curNode
	return head
