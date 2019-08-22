"""思路使用贪心算法 按照最大的纸币来进行找钱就能得到最少硬币数量"""


def solution(nums, aim):
	if len(nums) == 0 or aim < 0:
		return -1
	n = len(nums)
	m = float('Inf')
	dp = [[0 for i in range(aim + 1)] for j in range(len(nums))]
	for i in range(1, aim + 1):
		dp[0][i] = m
		if i - nums[0] >= 0 and dp[0][i - nums[0]] != m:
			dp[0][i] = dp[0][i - nums[0]] + 1
	left = 0
	for i in range(1, n):
		for j in range(1, aim + 1):
			left = m
			if j - nums[i] >= 0 and dp[i][j - nums[i]] != m:
				left = dp[i][j - nums[i]] + 1
			dp[i][j] = min(left, dp[i - 1][j])
	if dp[n - 1][aim] != m:
		return dp[n - 1][aim]
	else:
		return -1


def get_min_money(N):
	nums = [1, 4, 16, 64]
	aim = 1024 - N
	return solution(nums, aim)


class Solution:
	def twoSum(self, nums: list, target: int) -> list:
		for i in range(len(nums) - 1):
			for j in range(i + 1, len(nums)):
				if nums[i] + nums[j] == target:
					return [i, j]

a = Solution().twoSum([2,7,13,15],9)
print(a)


class A:
	
	def __init__(self, a):
		self.a = a


class B(A):
	
	def __init__(self, a, b, c):
		super().__init__(a)
		self.b = b
		self.c = c


b = B(1, 2, 3)
print(b.a)
print(b.b)
print(b.c)