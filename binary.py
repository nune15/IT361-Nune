def binary_search(zangvac, tarr):
    left = 0
    right = len(zangvac) - 1
    while left <= right:
        mid = (left + right) // 2
        if zangvac[mid] == tarr:
            return mid
        elif zangvac[mid] < tarr:
            left = mid + 1
        else:
            right = mid - 1

    return -1 
zangvac = [1, 3, 5, 7, 9, 11]
tarr = 9
print(binary_search(zangvac, tarr))