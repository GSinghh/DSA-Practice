#k is the window size
#slides 'window' across array
#k = 3
# i.e. [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10]


def slidingWindow(nums, k):
    for i in range(len(nums) - k + 1):
        print("Window: ", nums[i:i + k])
        
# slidingWindow([1,2,3,4,5,6,7,8,9,10], 3)

def sliding_window_sum(nums, k):
    res = 0
    window_sum = sum(nums[:k])
    res = max(res, window_sum)
    for i in range(k, len(nums)):
        window_sum += nums[i]
        window_sum -= nums[i - k]
        res = max(res, window_sum)
    return res
        
sliding_window_sum([1,4,5,67,4,1,7,9,1], 3)