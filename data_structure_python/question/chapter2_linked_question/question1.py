def print_common_part(head1, head2):
	"""大印两个链表相同的部分"""
	print("Common part:")
	while head1 is not None and head2 is not None:
		if head2.value < head1.value:
			head2 = head2.next
		elif head2.value == head1.value:
			print(head1.value)
			head1, head2 = head1.next, head2.next
		else:
			head1 = head1.next
	print("final")
