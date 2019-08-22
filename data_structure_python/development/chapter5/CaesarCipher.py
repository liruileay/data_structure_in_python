class CaesarCipher(object):
	'''凯撒加密实现'''
	
	def __init__(self, shift):
		'''初始化生成一个加密密钥和一个解密密钥'''
		encoder = [None] * 26
		decoder = [None] * 26
		for k in range(26):
			encoder[k] = chr((k + shift) % 26 + ord("A"))
			decoder[k] = chr((k - shift) % 26 + ord("A"))
		self._forward = encoder
		self._backward = decoder
	
	def encrypt(self, message):
		'''加密操作'''
		return self._transform(message, self._forward)
	
	def decrypt(self, secret):
		'''解密操作'''
		return self._transform(secret, self._backward)
	
	def _transform(self, original, code):
		'''加密解密的具体实现过程'''
		msg = list(original)
		for k in range(len(msg)):
			if msg[k].isupper():
				j = ord(msg[k]) - ord("A")
				msg[k] = code[j]
		return "".join(msg)


if __name__ == '__main__':
	cipher = CaesarCipher(15)
	massage = "I LOVE YOU123"
	secret = cipher.encrypt(massage)
	massage = cipher.decrypt(secret)
	print(secret)
	print(massage)


def the_same_count(i, a, b):
	count = 0
	for j in range(len(b)):
		if b[j] == a[j + i]:
			count += 1
	return count


def the_max_same_count_betweenab(a, b):
	"""a的长度是大于等于b的"""
	len_a = len(a)
	len_b = len(b)
	size = len_a - len_b
	if size == 0: return the_same_count(0, a, b)
	count = 0
	for i in range(size): # 找到如何才能最多
		count = the_same_count(i, a, b) if count < the_same_count(i, a, b) else count
	return count + size
