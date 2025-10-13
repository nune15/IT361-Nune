def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
        print(f"Step {i + 1}: {arr}")
    return arr
if __name__ == "__main__":
    nums = [10,25,36,78,95,85,25]
    sorted_nums = selection_sort(nums)
    print("Sorted array:", sorted_nums)
