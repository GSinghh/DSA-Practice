def prefixSum(nums):
    res = []
    currSum = 0
    for num in nums:
        currSum += num
        res.append(currSum)
    return res
