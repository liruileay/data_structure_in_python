import base64
import pickle

import redis

from sort.GeneralHashFunctions import rs_hash, js_hash, pjw_hash, elf_hash, bkdr_hash, sdbm_hash, djb_hash, dek_hash


class BloomFilterRedis(object):
	'''利用布隆过滤器的实现具体流程'''
	hash_list = [rs_hash, js_hash, pjw_hash, elf_hash, bkdr_hash, sdbm_hash, djb_hash, dek_hash]
	
	def __init__(self, key, port = '6379', password = 123456, host = '127.0.0.1'):
		'''key表示redis中的那个key对应的bit位的列表作为这个判别的容器'''
		self.key = key
		self.redis_conn = redis.StrictRedis(host = host, password = password, port = port, charset = 'utf-8')
	
	def _random_generator(self, hash_value, ):
		'''对hash进行取模确定他的位置'''
		return hash_value % (1 << 32)
	
	def do_filter(self, value, save = True):
		'''判断是否存在true表示存在False表示不存在save=Ture表示不存在就添加'''
		exists = True
		for hash in self.hash_list:
			hash_value = hash(value)
			index_value = self._random_generator(hash_value)
			if self.redis_conn.getbit(self.key, index_value) == 0:
				if save:
					self.redis_conn.setbit(self.key, index_value, 1)
				exists = False
		return exists


class Stu(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age


if __name__ == '__main__':
	'''对对象进行去重操作前一定要序列化'''
	bloom = BloomFilterRedis("bloom_obj")
	data = pickle.dumps(Stu("xiaohong", 18))
	data1 = base64.b64encode(data).decode()
	ret = bloom.do_filter(data1)
	print(ret)
	
	data = pickle.dumps(Stu("xiaohong", 18))
	data1 = base64.b64encode(data).decode()
	ret = bloom.do_filter(data1)
	print(ret)
	
	bloom = BloomFilterRedis("bloom_url")
	ret = bloom.do_filter("http://www.baidu.com")
	print(ret)
	ret = bloom.do_filter("http://www.baidu.com")
	print(ret)


