"""
换钱最少货币数
	[题目]
		给定数组arr,arr中所有的值都为正数且不重复.每个值代表一种面值的货币，每种面值的货币可以
		使用任意张，在给定一个整数aim代表要找的钱数，求组成aim最少货币数
"""


def min_coins(arr, aim):
	if arr is None or len(arr) == 0 or aim < 0:
		return -1
	n = len(arr)
	dp = [[0] * (aim + 1)] * n
	max = None
	for j in range(1, aim):
		dp[0][j] = max
		if j - arr[0] >= 0 and dp[0][j - arr[0]] != max:
			dp[0][j] = dp[0][j - arr[0]] + 1
	for i in range(1, n):
		for j in range(1, aim):
			left = max
			if j - arr[i] >= 0 and dp[i][j - arr[i]] != max:
				left = dp[i][j - arr[i]] + 1
			dp[i][j] = min(left, dp[i - 1][j])
	return dp[n - 1][aim] if dp[n - 1][aim] is not max else -1
