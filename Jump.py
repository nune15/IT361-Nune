import math

def jump_search(zangvac, tarr):
    n = len(zangvac)
    step = int(math.sqrt(n))
    start = 0

    while start < n and zangvac[min(step, n) - 1] < tarr:
        start = step
        step += int(math.sqrt(n))
        if start >= n:
            return -1
    while start < n and zangvac[start] < tarr:
        start += 1

    if start < n and zangvac[start] == tarr:
        return start 
    return -1
zangvac = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
tarr = 15

index = jump_search(zangvac, tarr)
print(index)
