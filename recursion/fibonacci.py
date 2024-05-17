def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fibonacci(n - 1) + fibonacci(n - 2)
    
    
def fibonacci_dp(n):
    dp = [0, 1, 1]
    for i in range(3, n + 1):
        val = dp[i - 1] + dp[i - 2]
        dp.append(val)
    
    return dp[n]

