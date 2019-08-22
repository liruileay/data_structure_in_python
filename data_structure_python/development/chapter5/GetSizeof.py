import sys

def Text(n):
	'''getsizeof只能获取列表对象本生的大小不能获取列表中元素的大小'''
	data = []
	for k in range(n):
		a = len(data)
		b = sys.getsizeof(data)
		print("Length: {0:3d}; Size in bytes: {1:4d}".format(a,b))
		data.append(k)
		
Text(20)