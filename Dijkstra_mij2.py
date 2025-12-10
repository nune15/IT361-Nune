def dijkstra(graph, start):
    dist = {v: float('inf') for v in graph}
    dist[start] = 0

    visited = set()

    while len(visited) < len(graph):
        u = None
        current_min = float('inf')

        for v in graph:
            if v not in visited and dist[v] < current_min:
                current_min = dist[v]
                u = v

        if u is None:
            break

        visited.add(u)

        for (nei, w) in graph[u]:
            if dist[u] + w < dist[nei]:
                dist[nei] = dist[u] + w

    return dist

graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('C', 5), ('D', 10)],
    'C': [('E', 3)],
    'D': [],
    'E': [('D', 4)]
}
print(dijkstra(graph, 'A'))
