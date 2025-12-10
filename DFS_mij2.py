graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}

visited = set()

def dfs(n):
    if n not in visited:
        print(n, end=" ")
        visited.add(n)
        for n1 in graph[n]:
            dfs(n1)

dfs('A')


            
