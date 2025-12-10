graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}

def bfs(start):
    visited = set()
    queue = [start]
    
    while queue:
        n = start.pop(0)
        if n not in visited:
            print(n, end="")
            visited.add(n)
            for n1 in graph[n]:
                queue.append(n1)
bfs('A')