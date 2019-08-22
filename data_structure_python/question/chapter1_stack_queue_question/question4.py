"""猫狗队列"""
from development.chapter6.ArrayQueue import Empty
from development.chapter7.LinkedQueue import LinkedQueue

"""

实现猫狗队列的实现要求如下
用户可以使用add方法将cat类或者dog类的实例放入队列中
用户可以调用pollAll方法，将队列中所有的实例按照队列的先后顺序依次弹出
用户可以调用pollDog方法，将队列中的dog类的实例按照队列的先后顺序依次弹出
用户可以调用pollCat方法，将队列中的cat类的实例按照队列的先后顺序依次弹出
用户可以调用isEmpoty来判断队列中是否有cat类或者dog列的实例
用户可以调用isDogEmpty方法来判断队列中是否有dog类的实例
用户可以调用isCatEmpty方法来判断队列中是否有cat类的实例

"""


class Pet(object):
	"""实现一个宠物类"""
	
	def __init__(self, type):
		self.type = type
	
	def get_pet_type(self):
		return self.type


class Dog(Pet):
	"""创建一个狗队列"""
	
	def __init__(self):
		super().__init__("dog")


class Cat(Pet):
	"""创建一个猫队列"""
	
	def __init__(self):
		super().__init__("Cat")


class PetEnterQueue(object):
	
	def __init__(self, pet, count):
		self.pet = pet
		self.count = count
	
	def get_pet(self):
		"""获取实例存储起来"""
		return self.pet
	
	def get_count(self):
		"""记录实例的数量"""
		return self.count
	
	def __str__(self):
		"""打印具体的名称"""
		return self.pet.get_pet_type()


class DogCatQueue(object):
	"""猫狗队列的具体实现"""
	
	def __init__(self):
		"""用两个队列来存储猫和狗的实例count表示整个猫狗队列中整个的元素的总合"""
		self.dogQ = LinkedQueue()
		self.catQ = LinkedQueue()
		self.count = 0
	
	def add(self, pet):
		"""实例对象添加进入队列中"""
		if pet.get_pet_type() == "dog":
			self.dogQ.enqueue(PetEnterQueue(pet, self.count))
			self.count += 1
		elif pet.get_pet_type() == "cat":
			self.catQ.enqueue(PetEnterQueue(pet, self.count))
			self.count += 1
		else:
			raise TypeError("只能是dog或者cat的实例")
	
	def poll_all(self):
		"""依次弹出猫狗队列中所有的元素"""
		if not self.catQ.is_empty() and not self.dogQ.is_empty():
			if self.dogQ.first().get_count() < self.catQ.first().get_count():
				return self.dogQ.dequeue().get_pet()
			else:
				return self.catQ.dequeue().get_pet()
		elif self.catQ.is_empty() and not self.dogQ.is_empty():
			return self.dogQ.dequeue().get_pet()
		elif self.dogQ.is_empty() and not self.catQ.is_empty():
			return self.catQ.dequeue().get_pet()
		else:
			raise Empty('queue is empty')
	
	def poll_dog(self):
		"""弹出狗队列中的元素"""
		if self.dogQ.is_empty():
			raise Empty('dogqueue is empty')
		return self.dogQ.dequeue().get_pet()
	
	def poll_cat(self):
		"""弹出猫队列中的元素"""
		if self.catQ.is_empty():
			raise Empty('catqueue is empty')
		return self.catQ.dequeue().get_pet()
	
	def is_empty(self):
		"""判断猫狗队列是否为空"""
		return self.count == 0
	
	def dog_is_empty(self):
		"""判断狗队列是否为空"""
		return self.catQ.is_empty()
	
	def cat_is_empty(self):
		"""判断毛队列是否为空"""
		return self.catQ.is_empty()
	


