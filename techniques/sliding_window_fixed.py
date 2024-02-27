#k is the window size
#slides 'window' across array
#k = 3
# i.e. [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10]


def slidingWindow(nums, k):
    for i in range(len(nums) - k + 1):
        print(nums[i:i + k])
        
slidingWindow([1,2,3,4,5,6,7,8,9,10], 3)