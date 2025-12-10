def bellman_ford(n, edges, start):
    
    INF = float('inf')
    dist = [INF] * n
    dist[start] = 0

    for _ in range(n-1):
        changed = False
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                changed = True
        if not changed:
            break

    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            return None 

    return dist

edges = [
    (0,1,6),
    (0,2,7),
    (1,2,8),
    (1,3,5),
    (1,4,-4),
    (2,3,-3),
    (2,4,9),
    (3,1,-2),
    (4,3,7)
]

print(bellman_ford(5, edges, 0))
