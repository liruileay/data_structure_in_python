"""

将一个单链表按照一个值划分为左边小、中间相等、右边大的形状

"""


def swap(node_arr, small, index):
	"""交换俩个变量的值"""
	node_arr[small], node_arr[index] = node_arr[index], node_arr[small]


def arrparition(node_arr, pivot):
	"""对数组进行排序小的放在pivot前面等于的放在pivot中间大于的放在pivot后面"""
	small = -1
	big = len(node_arr)
	index = 0
	while index is not big:
		if node_arr[index].value < pivot:
			small += 1
			swap(node_arr, small, index)
			index += 1
		elif node_arr[index].value == pivot:
			index += 1
		else:
			big -= 1
			swap(node_arr, big, index)


def list_partition1(head, pivot):
	"""将一个链表按照pivot分为左边小中间相等、右边大的     --->取出来排好序在重连"""
	if head is None:
		return head
	cur = head
	i = 0
	while cur is not None:
		i += 1
		cur = cur.next
	node_arr = [None] * i
	cur = head
	for i in range(len(node_arr)):
		node_arr[i] = cur
		cur = cur.next
	arrparition(node_arr, pivot)
	for i in range(len(node_arr)):
		"""将数组中的数拿出来进行节点的连接操作"""
		node_arr[i - 1].next = node_arr[i]
	node_arr[i - 1].next = None
	return node_arr[0]


def list_partition2(head, pivot):
	"""将一个链表按照pivot分为左边小中间相等右边大    --->利用三条链表操作"""
	sH = None
	sT = None
	eH = None
	eT = None
	bH = None
	bT = None
	while head is not None:
		if head.value > pivot:
			if sH is None or sT:
				sH = head
				sT = head
			else:
				sH.next = head
				sT = head
		if head.value == pivot:
			if eH is None or eT:
				eH = head
				eT = head
			else:
				eH.next = head
				eT = head
		if head.value < pivot:
			if bH is None or bT:
				bH = head
				bT = head
			else:
				bH.next = head
				bH = head
		head = head.next
	if sT is not None:
		sT.next = eH
		eT = eT if eT is not None else sT
	if eT is not None:
		eT.next = bH
	head = sH if sH is not None else eH if eH is not None else bH if bH is not None else None
	return head

