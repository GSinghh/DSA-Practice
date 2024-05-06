"""
This function will calculate the distinct ways to climb stairs to get
to a number "n"
"""
def climbStairs(n):
    dp = [0, 1, 2]
    for i in range(3, n + 1):
        val = dp[i - 1] + dp[i - 2]
        dp.append(val)
    return dp[n]
