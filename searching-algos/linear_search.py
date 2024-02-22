def linearSearch(target, vals) -> bool:
    for i in range(len(vals)):
        if vals[i] == target:
            return True
        
    return False

print(linearSearch(12, [1,2,3,4,5,6,7,8,9,10]))