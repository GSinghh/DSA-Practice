def binarySearch(target, vals) -> int:
    left, right = 0, len(vals) - 1
        
    while left <= right:
        midpoint = left + ((right - left) // 2)
        
        if vals[midpoint] > target:
            right = midpoint - 1
        elif vals[midpoint] < target:
            left = midpoint + 1
        else:
            return midpoint
    return - 1

print(binarySearch(4, [1,2,3,4,5,6,7,8,9,10]))

# The left pointer points to the last index where the target value is less than or equal to the element in the array.

# The right pointer points to the first index where the target value is greater than the element in the array.