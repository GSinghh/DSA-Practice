def bit_shifting():
    # Number before shift
    num = 19
    print(f"Original number: {num} (Binary: {bin(num)})")

    # Left shift by two places
    left_shift = num << 2
    print(f"Left shift by 2 bits: {left_shift} (Binary: {bin(left_shift)})")

    # Right shift by two places
    right_shift = num >> 2
    print(f"Right shift by 2 bits: {right_shift} (Binary: {bin(right_shift)})")

bit_shifting()