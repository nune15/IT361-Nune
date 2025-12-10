def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])
def graham(points):
    P = sorted(set(points))
    if len(P) <= 1:
        return P

    lower = []
    for p in P:
        while len(lower)>=2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(P):
        while len(upper)>=2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]
pts = [(0,0),(1,2),(2,1),(4,0),(2,-2),(1,-1)]
print(graham(pts))
