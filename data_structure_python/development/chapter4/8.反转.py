def reverse(S, start, end):
	if start < end-1:
		S[start], S[end-1] = S[end-1], S[start]
		reverse(S, start +1, end - 1)
	return S

print(reverse([8,7,6,5,4,3,2,1],0,8))
