def bad_fibonacci(n):
	if n < 1:
		return n
	return bad_fibonacci(n - 1) + bad_fibonacci(n - 2)

def good_fibonacci(n):
	if n <=1:
		return 0,1
	else:
		a,b = good_fibonacci(n-1)
	return a,b