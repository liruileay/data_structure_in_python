from collections import deque

# deque是一个封装好的双端队列

double_queue = deque(maxlen=10)
double_queue.append(1)
double_queue.appendleft(2)
# 多了的值会覆盖
for i in range(12):
	double_queue.appendleft(i)
print(double_queue)
