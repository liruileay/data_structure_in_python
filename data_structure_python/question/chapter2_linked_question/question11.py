"""两个单链表的相交问题
解答:
	这道题需要分析的情况非常多,同时因为有额外的空间复杂度O(1)的限制,所以实现起来比较困难
	本问题可以拆分成三个子问题,每个问题都可以作为一道独立的算法题
	我们知道 一个有环链表和一个无环链表是不会有交点的
	问题一:
		如何判断一个链表是否有环,如果有返回第一个入环的节点,没有就返回None
		### 解决方式:设置一个慢指针和一个块指针,在开始的时候快指针和慢指针都指向头节点,然后快指针每次移动两个,
					慢指针每次移动一个当两个指针第一次相交的时候快指针回到头节点,然后快指针变成慢指针,快指针
					和慢指针一起走,当两个指针相交的时候就是该链表的第一个入环节点
	问题二:
		如何判断两个无环链表相交,相交则返回相交的第一个节点,不相交则返回None
		两个链表从相交的节点后面的所以节点是一样的
		
		
	问题三:
		如何判断连个有环链表是否相交,相交则返回第一个相交的节点,不相交则返回None
		我们得到一个链表的入环的位置 如果loop1 == loop2那么两个链表的拓扑结构 如下
								\        /
								 \      /
								  \node/
								  圆形
								  
"""


def get_loop_node(head):
	"""判断一个链表是否有环如果有环就返回第一个入环的节点"""
	if head is None or head.next is None or head.next.next is None:
		return None
	n1 = head.next
	n2 = head.next.next
	while n1 is not n2:
		if n1.next is None or n2.next.next is None:
			return
		n2 = n2.next.next
		n1 = n1.next
	n2 = head
	while n1 is not n2:
		n1 = n1.next
		n2 = n2.next
	return n1


def no_loop(head1, head2):
	'''两个无环链表是不是相交的逻辑'''
	if head1 is None or head2 is None:
		return None
	cur1 = head1
	cur2 = head2
	n = 0
	while cur1.next is not None:
		cur1 = cur1.next
		cur1 += 1
	while cur2.next is not None:
		cur2 = cur2.next
		cur2 -= 1
	if cur2 is not cur1:
		return None
	cur1 = head1 if n > 0 else head2
	cur2 = head2 if cur1 is head1 else head2
	n = abs(n)
	while n != 0:
		cur1 = cur1.next
		n -= 1
	while cur1 is not cur2:
		cur1 = cur1.next
		cur2 = cur2.next
	return cur1


def both_loop(head1, head2, loop1, loop2):
	'''判断两个有环链表是否相交现在已经的到连个链表的循环节点loop'''
	if loop2 is loop1:  # 表示一定有交点
		cur1 = head1
		cur2 = head2
		n = 0
		while cur1 is not loop1:
			cur1 = cur1.next
			n += 1
		while cur2 is not loop2:
			cur2 = cur2.next
			n -= 1
		cur1 = head1 if n > 0 else head2
		cur2 = head2 if cur1 is head1 else head1
		n = abs(n)
		while n != 0:
			cur1 = cur1.next
			n -= 1
		while cur1 is not cur2:
			cur1 = cur1.next
			cur2 = cur2.next
		return cur1
	else:
		cur1 = loop1.next
		while cur1 != loop1:
			if cur1 is loop2:
				return loop1
			else:
				cur1 = cur1.next
		return None


def get_intersect_node(head1, head2):
	'''返回两个链表相交的部分'''
	if head1 is None or head2 is None:
		return None
	loop1 = get_loop_node(head1)
	loop2 = get_loop_node(head2)
	if loop1 is not None and loop2 is not None:
		return both_loop(head1, head2, loop1, loop2)
	if loop1 is None and loop1 is None:
		return no_loop(head1, head2)
	return None

