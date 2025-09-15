def partition(arr, skizb , verj):
    pivot = arr[verj]
    i = skizb - 1

    for j in range(skizb,verj):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[verj] = arr[verj], arr[i+1]
    return i+1

def quick_sort(arr, skizb,verj):
    if skizb< verj:
        p = partition(arr, skizb, verj)
        quick_sort(arr,skizb, p-1)
        quick_sort(arr, p+1, verj)

arr = [14,25,87,6,98,2]
quick_sort(arr, 0, len(arr)-1)
print("arr=",arr)
