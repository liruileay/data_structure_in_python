import os

def disk_usage(path):
	total = os.path.getsize(path)
	if os.path.isdir(path):
		for filename in os.listdir(path):
			child_path = os.path.join(path, filename)
			total += disk_usage(child_path)
	print("{0:7}".format(total),path)
	return total


disk_usage(os.path.dirname(os.path.abspath("__file__")))