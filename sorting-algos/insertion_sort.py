def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

arr = [53, 23, 12, 1, 22, 81, 12, 18]
print(f"Original Array: {arr}")
print(f"Sorted Array: {insertion_sort(arr)}")