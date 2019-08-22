"""如何用一个递归函数和栈栈操作逆序一个栈"""
from development.chapter6.ArrayStack import ArrayStack


def get_and_remove_last_element(stack):
	"""找到栈中的最后一个元素"""
	result = stack.pop()
	if stack.is_empty():
		return result
	else:
		last = get_and_remove_last_element(stack)
		stack.push(result)
		return last


def reverse_stack(stack):
	"""将一个栈进行反转操作"""
	if stack.is_empty():
		return
	element = get_and_remove_last_element(stack)
	reverse_stack(stack)
	stack.push(element)


if __name__ == '__main__':
	stack = ArrayStack()
	for i in range(10):
		stack.push(i)
	reverse_stack(stack)
	for i in range(10):
		print(stack.pop())
