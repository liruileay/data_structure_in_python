"""
按位或运算 |
1|1=1     0|1=1     1|0=1     0|0=0
"""

"""
按位与运算符 & 指的是最后一位
1&1=1    0&1=0     0&0=0     1&0=0
"""
def is_odd(n):
    """
    判断奇偶性
    """
    if n&1 == 1:
        print("奇数")
    else:
        print("偶数")

def totle_num(n):
    """
    整数n的二进制中1的个数 
    n&(n-1)这个式子什么作用？把n的二进制数字中最右边的1变为0
    """
    count = 0
    while n:
        count+=1
        n = n&(n-1)
    print(count)
    


"""
异或运算 ^
1^1=0     0^1=1     1^0=1     0^0=0

异或的几条性质:
1、交换律  a^b = b^a
2、结合律  a^b^c = a^(b^c)
>>>>>>   x^0=x    x^x=0
"""
a = 1
b = 2
"""
交换a和b的值的方法
a = a^b
b = a^b
a = a^b

具体过程
b = a^b^b = a
a = a^b^a = b
"""

def singleNumber(nums):
    """
    [0,1,2,0,1,2,3]
    给定一个非空整数列表，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。leetcode 136
    """
    ret = 0
    for x  in nums:
        ret = ret^x
    return ret
    





