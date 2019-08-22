import random


class Vector(object):
	
	def __init__(self, size):
		self._vector = [0] * size
	
	def __len__(self):
		return len(self._vector)
	
	def __add__(self, other):
		"""定义相见的行为"""
		if len(self) != len(other):
			raise ValueError("不同维的向量不能相加")
		result = Vector(len(self))
		for j in range(len(self._vector)):
			result[j] = self._vector[j] + other[j]
		return result
	
	def __getitem__(self, i):
		return self._vector[i]
	
	def __setitem__(self, key, value):
		self._vector[key] = value
	
	def __eq__(self, other):
		return self._vector == other._vector
	
	def __ne__(self, other):
		"""判断是否相等不等为True相等为False"""
		return not self == other
	
	def __str__(self):
		return "<" + str(self._vector) + ">"
	
	# def __repr__(self):
	# 	return "<" + str(self._vector) + ">"

v = Vector(5)
v[1]=4

v1 = Vector(5)
for i in range(5):
	v1[i] = random.randint(1,10)
print(v)
print(v1)
print(v+v1)