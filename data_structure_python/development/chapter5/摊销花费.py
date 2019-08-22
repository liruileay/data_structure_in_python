from time import time


def compute_average(n):
	data = []
	start = time()
	for k in range(n):
		data.append(k)
	end = time()
	print(end - start)


def compute_average1(n):
	data1 = [i for i in range(n)]
	data = []
	start = time()
	data.extend(data1)
	end = time()
	print(end - start)


compute_average(100000000)
compute_average1(100000000)
