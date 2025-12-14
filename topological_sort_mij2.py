def topological_sort(graph):
    indegree = {v: 0 for v in graph}
    for v in graph:
        for nei in graph[v]:
            indegree[nei] += 1

    queue = [v for v in graph if indegree[v] == 0]

    order = []
    while queue:
        v = queue.pop(0)
        order.append(v)

        # decrease indegree of neighbors
        for nei in graph[v]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                queue.append(nei)

    return order

graph = {
    "A": ["C"],
    "B": ["C", "D"],
    "C": ["E"],
    "D": ["F"],
    "E": ["H", "F"],
    "F": ["G"],
    "G": [],
    "H": []
}
order = topological_sort(graph)

print("Topological Order:")
print(order)
