def postfixSum(nums):
    res = []
    currSum = 0
    for i in range(len(nums) -1, -1, -1):
        currSum += nums[i]
        res.append(currSum)
    return res