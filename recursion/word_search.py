def word_search(board, word) -> bool:
    rows = len(board)
    cols = len(board[0])
    visited = set()
    
    def dfs(row, col, word_index):
        """ 
        Recursive Case 1, if the current index is equal to the length of the word we are looking for
        This means we have found the word within the board and we can return true
        """
        
        if word_index == len(word):
            return True
        
        """
        Recursive Case 2, The current position cannot be out of bounds, this is done by checking 
        If our current row or col position is less than 0 meaning that it's less than the first
        index of the array, We also check if our current position is greater than or equal to the 
        right bound which is the last index in our array
        The last thing we check is whether our current position is already in our visited set,
        Meaning that this position has already been visited and we cannot use it again 
        """
        
        if (row < 0 or row >= rows or
            col < 0 or col >= cols or 
            word[word_index] != board[row][col]
            or (row, col) in visited):
            return False 
        """
        If our position is in bounds and has not been visited before, we can add that 
        position to our visited set 
        """
        visited.add((row, col))
        res = (
            dfs(row + 1, col, word_index + 1) or
            dfs(row - 1, col, word_index + 1) or 
            dfs(row, col + 1, word_index + 1) or 
            dfs(row, col - 1, word_index + 1)
        )
        visited.remove((row, col))
        return res
    
    for row in range(len(board)):
        for col in range(len(board[0])):
            if dfs(row, col, 0):
                return True
    return False
    
    
board = [["A", "B", "C", "E"],["S", "F", "C", "S"],["A", "D", "E", "E"]]
word = "ABCCED"
print(word_search(board, word))