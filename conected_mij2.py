def connected_components(graph):
    visited = set()
    components = []
    for v in graph:
        if v not in visited:
            stack = [v]
            comp = []

            while stack:
                u = stack.pop()
                if u not in visited:
                    visited.add(u)
                    comp.append(u)
                    stack.extend(graph[u])

            components.append(comp)

    return components
graph = {
    0: [1],
    1: [0],
    2: [3],
    3: [2],
    4: []
}
result = connected_components(graph)

print("Connected Components:")
for c in result:
    print(c)
