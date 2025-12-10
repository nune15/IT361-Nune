def connected_components_bfs(graph):
    visited = set()
    components = []

    for v in graph:
        if v not in visited:
            queue = [v] 
            comp = []

            while queue:
                u = queue.pop(0)
                if u not in visited:
                    visited.add(u)
                    comp.append(u)
                    for nei in graph[u]:
                        if nei not in visited:
                            queue.append(nei)

            components.append(comp)

    return components


graph = {
    0: [1],
    1: [0],
    2: [3],
    3: [2],
    4: []
}

print(connected_components_bfs(graph))
