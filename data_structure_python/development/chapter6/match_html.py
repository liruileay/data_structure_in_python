from development.chapter6.ArrayStack import ArrayStack


def is_matched_html(raw):
	"""匹配html标签"""
	S = ArrayStack()
	j = raw.find("<")
	while j != -1:
		k = raw.find(">", j + 1)
		if k == -1:
			return False
		tag = raw[j + 1:k]
		if not tag.startwith("/"):
			S.push(tag)
		else:
			if S.is_empty():
				return False
			if S.pop() != tag[1:]:  # tag[1:]表示吧第一个/给去掉
				return False
		j = raw.find("<", k + 1)
	return S.is_empty()
