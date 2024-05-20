def permutations(nums):
    res, sol = [], []
    
    
    
    # Backtrack function does DFS on decision tree
    def backtrack():
        # Base case for recursive case
        # If len of the solution is equal to 
        # length of numbers in num, meaning
        # We have exhaust all possible choices 
        if len(sol) == len(nums):
            res.append(sol[:])
            return
        
        # Iterate over each value within the list
        # If the value is not within the list
        # Append it and call the backtrack function again
        for val in nums:
            if val not in sol:
                sol.append(val)
                backtrack()
                sol.pop()
            
    backtrack()
    return res
    
nums = [1, 2, 3]

print(permutations(nums))