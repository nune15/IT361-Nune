def orientation(p, q, r):
    return (q[0]-p[0])*(r[1]-p[1]) - (q[1]-p[1])*(r[0]-p[0])


def jarvis(points):
    n = len(points)
    if n < 3:
        return points
    
      l = 0
    for i in range(1, n):
        if points[i][0] < points[l][0]:
            l = i
    
    hull = []
    p = l
    
    while True:
        hull.append(points[p])
        q = (p+1) % n
        
        for i in range(n):
            if orientation(points[p], points[q], points[i]) < 0:
                q = i
        
        p = q
        if p == l: break

    return hull

pts = [
    (0,0),(1,2),(2,1),(3,3),
    (4,0),(2,-2),(3,-1),(1,-1)
]

hull = jarvis(pts)
print("Convex Hull:", hull)
