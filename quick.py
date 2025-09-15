def quick_sort(arr):
    if len(arr) <=1:
        return arr
    
    pivot = arr[0]

    left = []
    right = []
    equal = []

    for x in arr:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
        else:
            equal.append(x)

    sorted_left = quick_sort(left)
    sorted_right = quick_sort(right)

    return sorted_left + equal + sorted_right

arr = [78,14,25,36,16]

print("arr=", arr)
print("nor", quick_sort(arr))