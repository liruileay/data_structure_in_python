# 检测元素的唯一性
#
# 1.只有一个元素元素就是唯一的
# 2.元素在后n-1个是唯一的
# 3.元素在前n-1个是唯一的
# 4.最后一个元素不等于第一个元素

def unique(S, start, end):
	if end - start == 0:return True
	elif not unique(S,start+1,end):return False
	elif not unique(S,start,end-1):return False
	else: return S[start] !=S[end-1]
