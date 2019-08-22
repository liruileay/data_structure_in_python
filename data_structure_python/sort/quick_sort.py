import random


# def partition(list, left, right):
# 	"""随机快排的分区操作"""
# 	left_cur, right_cur, cur, item = left - 1, right + 1, left, list[0]
# 	while cur < right_cur:
# 		while cur < right_cur and list[cur] < item:
# 			left_cur += 1
# 			list[left_cur], list[cur] = list[cur], list[left_cur]
# 			cur += 1
# 		while cur < right_cur and list[cur] > item:
# 			right_cur -= 1
# 			list[right_cur], list[cur] = list[cur], list[right_cur]
# 		while cur < right_cur and list[cur] == item:
# 			cur += 1
# 	print(left_cur, right_cur)
# 	return [left_cur, right_cur]
#
#
# def QuickSort_resursion(list, left, right):
# 	"""随机快速排序的递归实现"""
# 	if right <= left:
# 		return
# 	result = partition(list, left, right)
# 	QuickSort_resursion(list, left, result[0])
# 	QuickSort_resursion(list, result[1], right)


# def QuickSort(list):
# 	"""随机快速排序的非递归实现"""
# 	left, right = 0, len(list) - 1
# 	queue = []
# 	queue.append(left)
# 	queue.append(right)
# 	while queue:
# 		right = queue.pop()
# 		left = queue.pop()
# 		result = partition(list, left, right)
# 		if result[0] > left:
# 			queue.append(left)
# 			queue.append(result[0])
# 		if result[1] < right:
# 			queue.append(result[1])
# 			queue.append(right)
# 	return list


# def main():
# 	list = [random.randint(0, 1000) for i in range(100)]
# 	list1 = QuickSort(copy.deepcopy(list))
# 	item = sorted(copy.deepcopy(list))
# 	QuickSort_resursion(list, 0, len(list) - 1)
# 	for i in range(len(list)):
# 		if list[i] == item[i] == list1[i]:
# 			continue
# 		else:
# 			raise ValueError("Failure")
# 	print("Success")


#快排的主函数，传入参数为一个列表，左右两端的下标
def QuickSort(list,low,high):
    if high > low:
        #传入参数，通过Partitions函数，获取k下标值
        k = Partitions(list,low,high)
        #递归排序列表k下标左侧的列表
        QuickSort(list,low,k-1)
        # 递归排序列表k下标右侧的列表
        QuickSort(list,k+1,high)

def Partitions(list,low,high):
    left = low
    right = high
    #将最左侧的值赋值给参考值k
    k = list[low]
    #当left下标，小于right下标的情况下，此时判断二者移动是否相交，若未相交，则一直循环
    while left < right :
        #当left对应的值小于k参考值，就一直向右移动
        while list[left] <= k:
            left += 1
        # 当right对应的值大于k参考值，就一直向左移动
        while list[right] > k:
            right = right - 1
        #若移动完，二者仍未相遇则交换下标对应的值
        if left < right:
            list[left],list[right] = list[right],list[left]
    #若移动完，已经相遇，则交换right对应的值和参考值
    list[low] = list[right]
    list[right] = k
    #返回k值
    return right

list_demo = [6,1,2,7,9,3,4,5,10,8,4545,54,5,4,5454,444]
print(list_demo)
QuickSort(list_demo,0,15)
print(list_demo)
