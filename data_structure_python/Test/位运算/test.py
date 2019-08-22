# a = [101, 100, 108, 300, 1000, 7, 7, 1000, 101]
#
# x = [0] * 1001
#
# for i in a:
#     x[i] += 1
#
# for i in range(0, len(x)):
#     if x[i] > 0:
#         print(i, x[i])
# ord返回对应的编码顺序  ord("v") = 118

x = "itheimaheloworld"
list1 = [0] * 1000
for s in x:
    list1[ord(s)] += 1

for i in range(0, len(list1)):
    if list1[i] > 0:
        print(chr(i), list1[i])

