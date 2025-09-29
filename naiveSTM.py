def matching(text,pattern):
    n= len(text)
    m = len(pattern)

    for i in range(n-m-1):
        for j in range(m):
            if text[i+j] != pattern[j]:
                break
            else:
                print("Pattern occurs at ",i)

text = "aababbbahhaja"
pattern = "bba"
matching(text, pattern)