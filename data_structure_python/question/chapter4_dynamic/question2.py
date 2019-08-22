"""
矩阵的最小路径和
	[题目]
		给定一个矩阵m,从左上角开始每次只能向右或者向下走,最后到达右下角的位置,路径上所有的数字加起来
		就是路径的和,返回所有的路径中最小的路径和。
	
	【举例】
	如果给定的m如下:
	1   3   5   9
	8   1   3   4
	5   0   6   1
	8   8   4   0
	路径1，3，1，0，6，1，0是所有路径和中最小的一个,所以返回12
	
"""


def min_path_sum1(arr):
	"""动态规划解决这个问题"""
	if len(arr) == 0 or arr is None:
		return 0
	row = len(arr)
	col = len(arr[0])
	dp = [[0] * col] * row
	for i in range(1, row):
		dp[i][0] = dp[i - 1][0] + dp[i][0]
	for j in range(1, col):
		dp[0][j] = dp[0][j - 1] + dp[0][j]
	for i in range(1, row):
		for j in range(1, col):
			dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + dp[i][j]
	return dp[row - 1][col - 1]

