"""
	Morris 遍历的具体实现
	Morris遍历的实质就是避免使用栈结构,而是让下层到上层右指针,具体是通过让底层指向None的指针指回上层的节点

"""


class MorrisPreOrder(object):
	
	def morris_pre_order(self, head):
		"""morris遍历的先序遍历"""
		if head is None:
			return
		cur1 = head
		while cur1 is not None:
			cur2 = cur1.left
			if cur2 is not None:
				while cur2.right is not None and cur2.right is not cur1:
					cur2 = cur2.right
				if cur2.right is None:
					cur2.right = cur1
					yield cur1.value
					cur1 = cur1.left
					continue
				else:
					cur2.right = None
			else:
				yield cur1.value
			cur1 = cur1.right


class MorrisInOrder(object):
	
	def morris_in_order(self, head):
		"""Morris遍历的中序遍历"""
		if head is None:
			return
		cur1 = head
		while cur1 is not None:
			cur2 = cur1.left
			if cur2 is not None:
				while cur2.right is not None and cur2.right is not cur1:
					cur2 = cur2.right
				if cur2.right is None:
					cur2.right = cur1
					cur1 = cur1.left
					continue
				else:
					cur2.right = None
			yield cur1.value
			cur1 = cur1.right


class MorrisPosOrder(object):
	
	def reverse_edge(self, fro):
		pre = None
		while fro is not None:
			next = fro.right
			fro.right = pre
			pre = fro
			fro = next
		return pre
	
	def print_edge(self, head):
		tail = self.reverse_edge(head)
		cur = tail
		while cur is not None:
			yield cur.value
			cur = cur.right
		self.reverse_edge(tail)
	
	def morries_pos_order(self, head):
		"""morris遍历的后序遍历"""
		if head is None:
			return
		cur1 = head
		while cur1 is not None:
			cur2 = cur1.left
			if cur2 is not None:
				while cur2.right is not None and cur2.right is not cur1:
					cur2 = cur2.right
				if cur2.right is None:
					cur2.right = cur1
					cur1 = cur1.left
					continue
				else:
					cur2.right = None
					self.print_edge(cur1.left)
			cur1 = cur1.right
