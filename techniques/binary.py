def hamming_weight(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

# Example usage:
number = 55
print(hamming_weight(number)) 