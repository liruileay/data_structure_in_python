from development.chapter6.ArrayStack import ArrayStack


def is_matched(expr):
	'''利用栈进行匹配'''
	lefty = '({['
	righty = ')}]'
	S = ArrayStack()
	for c in expr:
		if c in lefty:
			S.push(c)
		elif c in righty:
			if S.is_empty():
				return False
			if righty.index(c) != lefty.index(S.pop()):
				return False
	return S.is_empty()

result = is_matched("{{{[[[ftwrtertert]]]}}}")
print(result)