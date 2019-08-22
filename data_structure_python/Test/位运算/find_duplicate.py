"""
1. 给定一个包含 0..n 中 n 个数的列表，找出 0 .. n 中没有出现在序列中的那个数。 leetcode 268
[1,3,0] 2
0^1^2^3^1^3^0    2

ret = 0
for i in range(0,n+1)
    ret ^= i

for i in range(0,len(nums)):
    ret ^= nums[i]

return ret

2. 1-n 放在含有 n+1 个元素的列表中，只有唯一的一个元素值重复，其它均只出现一次．
   每个列表元素只能访问一次，设计一个算法，将它找出来；不用辅助存储空间。 进阶版 leetcode 287
[1,2,2,3] 2 
0^1^2^3^1^2^2^3 = 2
"""

def func1(nums):
    fast = 0
    slow = 0
    while True:
        fast = nums[nums[fast]]
        slow = nums[slow]
        if fast == slow:
            break
    fast = 0
    while True:
        fast = nums[fast]
        slow = nums[slow]
        if fast == slow:
            return fast

