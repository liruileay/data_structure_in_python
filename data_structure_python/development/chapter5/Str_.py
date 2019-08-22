document = "fsdfwe   fNKHD  OJKIUS sdhf OofsfkFKSF 1423dnfdkgJDiofh"
def bad_way(document):
	"""去掉字符串中的空格"""
	letters = ""
	for c in document:
		if c.isalpha():
			letters +=c
	print(letters)

def good_way(document):
	"""去掉字符串中的空格"""
	temp = []
	for c in document:
		if c.isalpha():
			temp.append(c)
	letters = "".join(temp)
	print(letters)

def best_way(document):
	print("".join([c for c in document if c.isalpha()]))

bad_way(document)
good_way(document)
bad_way(document)