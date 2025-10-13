def boyer_moore_bad_character(T: str, P: str):
    n, m = len(T), len(P)
    last = {}
    for i in range(m):
        last[P[i]] = i
    s = 0 

    while s <= n - m:
        j = m - 1
        while j >= 0 and P[j] == T[s + j]:
            j -= 1
        if j < 0:
            return s
        else:
            bad_char = T[s + j]
            shift = j - last.get(bad_char, -1)
            s += max(1, shift)
    return None
T = "HERE IS A SIMPLE EXAMPLE"
P = "EXAMPLE"
print(boyer_moore_bad_character(T, P))
