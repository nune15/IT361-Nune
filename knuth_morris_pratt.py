def kmp_search(text, pattern):
    lps = [0] * len(pattern)
    j = 0  
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j != 0:
                j = lps[j-1]
            else:
                lps[i] = 0
                i += 1
    i = j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == len(pattern):
            print("Pattern found at index", i - j)
            j = lps[j-1]
        elif i < len(text) and text[i] != pattern[j]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
text = "BABACABBABACABB"
pattern = "ACA"
kmp_search(text, pattern)
