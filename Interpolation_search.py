def interpolation_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high and x >= arr[low] and x <= arr[high]:
        if arr[high] == arr[low]:
            if arr[low] == x:
                return low
            else:
                return -1
        pos = low + ((x - arr[low]) * (high - low)) // (arr[high] - arr[low])
        if arr[pos] == x:
            return pos
        elif arr[pos] < x:
            low = pos + 1
        else:
            high = pos - 1

    return -1
arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
x = 70
result = interpolation_search(arr, x)
if result != -1:
    print(f"Արժեքը գտնվեց {result} ինդեքսում։")
else:
    print("Արժեքը չի գտնվել։")
