"""环形单链表的约瑟夫问题
题目:
	据说著名犹太人历史学家Josephus有过以下故事:在罗马人占领乔塔帕特后,39个犹太人
	于Josephus及他的朋友躲到一个洞中,39个犹太人决定宁愿死也不要被敌人抓到,于是决定
	了一个自杀的方式,41个人排成一个圆圈,由第一人开始报数,报数到3的就自杀,然后在由下
	一个人报1,报数到3的人再自杀,这样依次下去,直到剩下最后一个人是,那个人可以自由选择
	自己的命运。这就是著名的约瑟夫问题。现在请用单向环形链表描述该结构并呈现整个自杀过程
"""


def josephus_kill1(head, m):
	"""约瑟夫问题的第一种解法 其中循环链表的最后一个节点的next指针指向head"""
	if head is None or head is head.next or m < 1:
		return head
	last = head
	while last.next is not head:
		last = last.next
	count = 0
	while last is not head:
		count += 1
		if count == m:
			last.next = head.next
			count = 0
		else:
			last = last.next
		head = last.next
	return head


def getLive(temp, m):
	"""递归得到唯一能够存活下来的那个节点的位置"""
	if m == 1:
		return 1
	return (getLive(temp - 1, m) + m - 1) % temp + 1


def josephus_kill2(head, m):
	"""约瑟夫问题的进阶解法 """
	if head is None or head.next is head or m < 1:
		return head
	cur = head.next
	temp = 1
	while cur is not head:
		temp += 1
		cur = cur.next
	temp = getLive(temp, m)
	while temp != 0:
		temp -= 1
		head = head.next
	head.next = head
	return head


