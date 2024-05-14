def matrix_binary_search(matrix, target):
    # Checking to see if if matrix is not empty or if row within the matrix is not empty
    if not matrix or not matrix[0]:
        return False
    
    # Get total number of rows and columns 
    rows, cols = len(matrix), len(matrix[0])
    
    # Start left pointer at beginning, start right pointer at last index
    left, right = 0, (rows * cols) - 1
    
    while left <= right:
        # Calculating midpoint
        # Using midpoint calcualtion to get value at midpoint
        mid_index = (left + right)  // 2 
        
        # mid_index // cols will give row mapping
        # mid_index % cols will give column mapping
        mid_val = matrix[mid_index // cols][mid_index % cols]
        
        # Binary search implentation remains the same
        if mid_val == target:
            return True
        elif mid_val < target:
            left = mid_index + 1
        else:
            right = mid_index - 1
            
    return False

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
target = 12

print(matrix_binary_search(matrix, target))