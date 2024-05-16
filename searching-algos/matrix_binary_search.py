"""
This version is for a matrix that is sorted in normal ascending order
Time Complexity(O(log n * m))
Space Complexity(O(1))
"""
def matrix_binary_search_version_one(matrix, target):
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




"""
This version is for a matrix with these properties:
- Integers in each row are sorted in ascending from left to right.
- Integers in each column are sorted in ascending from top to bottom.
Time Complexity(O(n + m))
Space Complexity(O(1))
"""
def matrix_binary_search_version_two(matrix, target):
    # Checking to see if if matrix is not empty or if row within the matrix is not empty
    if not matrix or not matrix[0]:
        return False
    
    # Get total number of rows and columns 
    rows, cols = len(matrix), len(matrix[0])
    
    # Start row at first index in first row, start col at last index in the first row
    row, col = 0, cols - 1
    
    #While both row and col are in bounds
    while row < rows and col >= 0:
        mid_val = matrix[row][col]
        
        if mid_val == target:
            return True
        elif mid_val < target:
            row += 1
        else:
            col -= 1
    return False
    