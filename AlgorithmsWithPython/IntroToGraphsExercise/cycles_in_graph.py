graph = {}

def dfs(node, graph, visited, cycles):
    if node in cycles:
        raise Exception
    if node in visited:
        return
    visited.add(node)
    cycles.add(node)
    for child in graph[node]:
        dfs(child, graph, visited, cycles)

    cycles.remove(node)

while True:
    line = input()
    if line == 'End':
        break
    source, destination = line.split('-')
    if source not in graph:
        graph[source] = []
    if destination not in graph:
        graph[destination] = []
    graph[source].append(destination)

#print(graph)
visited = set()
try:
    for node in graph:
        dfs(node, graph, visited, set())
    print('Acyclic: Yes')
except Exception:
    print('Acyclic: No')





for node in graph:
    dfs(node, graph, visited, set())