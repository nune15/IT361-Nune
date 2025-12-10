def intersect(a,b,c,d):

    def orient(p, q, r):
        v = (q[0]-p[0])*(r[1]-q[1]) - (q[1]-p[1])*(r[0]-q[0])
        return (v>0) - (v<0)

    def onseg(p,q,r):
        return min(p[0],r[0]) <= q[0] <= max(p[0],r[0]) and \
               min(p[1],r[1]) <= q[1] <= max(p[1],r[1])

    o1=orient(a,b,c); o2=orient(a,b,d)
    o3=orient(c,d,a); o4=orient(c,d,b)

    if o1!=o2 and o3!=o4: return True

    if o1==0 and onseg(a,c,b): return True
    if o2==0 and onseg(a,d,b): return True
    if o3==0 and onseg(c,a,d): return True
    if o4==0 and onseg(c,b,d): return True

    return False

A=(1,1); B=(4,4)
C=(1,8); D=(2,4)

print(intersect(A,B,C,D))
