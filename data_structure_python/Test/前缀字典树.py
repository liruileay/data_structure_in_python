class TrieNode(object):
	'''前缀字典树'''
	def __init__(self, path, end, nexts):
		self.path = path
		self.end = end
		self.next = nexts
	
	