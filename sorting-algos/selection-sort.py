def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
    return arr

arr = [64, 25, 12, 13, 22, 11]
print(f"Original Array: {arr}")
print(f"Sorted Array: {selection_sort(arr)}")