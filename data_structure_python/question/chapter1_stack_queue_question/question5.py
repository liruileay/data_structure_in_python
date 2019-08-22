"""用一个栈来实现另一个栈的排序"""
from development.chapter6.ArrayStack import ArrayStack


def stack_sort(stack):
	"""利用一个栈来对另一个栈进行排序"""
	help = ArrayStack()
	while not stack.is_empty():
		cur = stack.pop()
		while not help.is_empty() and help.top() < cur:
			stack.push(help.pop())
		help.push(cur)
	while not help.is_empty():
		print(help.pop())


if __name__ == '__main__':
	L = [2, 4, 6, 21, 45, 3, 54, 7]
	stack = ArrayStack()
	for i in L:
		stack.push(i)
	stack_sort(stack)
