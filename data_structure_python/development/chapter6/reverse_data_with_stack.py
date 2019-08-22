from development.chapter6.ArrayStack import ArrayStack


def reverse_file(filename):
	'''利用栈文件内容进行反转'''
	S = ArrayStack()
	original = open(filename)
	for line in original:
		S.push(line.rstrip("\n"))
	original.close()
	
	output = open(filename, "w")
	while not S.is_empty():
		output.write(S.pop() + "\n")
	output.close()


reverse_file("text.txt")