import threading


def lock_func(func):
	func.__lock__ = threading.Lock()
	
	def single_lock_func(cls, *args, **kwargs):
		with func.__lock__:
			return func(cls, *args, **kwargs)
	
	return single_lock_func


class SingleSafeInstance(object):
	"""线程安全的单例"""
	
	@lock_func
	def __new__(cls, *args, **kwargs):
		if not hasattr(cls, "instance"):
			cls.instance = super().__new__(cls)
		return cls.instance
