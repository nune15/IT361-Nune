def ternary_search(zangvac, tarr):
    left = 0
    right = len(zangvac) - 1

    while left <= right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        if zangvac[mid1] == tarr:
            return mid1

        if zangvac[mid2] == tarr:
            return mid2
        if tarr < zangvac[mid1]:
            right = mid1 - 1
        elif tarr > zangvac[mid2]:
            left = mid2 + 1

        else:
            left = mid1 + 1
            right = mid2 - 1

    return -1
zangvac = [1, 3, 5, 7, 9, 11, 13]
tarr = 5
print(ternary_search(zangvac, tarr)) 
