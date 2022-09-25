nodes = int(input())
graph = {}
edges = []
'''
8
1 -> 2 5 4
2 -> 1 3
3 -> 2 5
4 -> 1
5 -> 1 3
6 -> 7 8
7 -> 6 8
8 -> 6 7

'''
'''
14
K -> X J
J -> K N
N -> J X L M
X -> K N Y
M -> N I
Y -> X L
L -> N I Y
I -> M L
A -> Z Z Z
Z -> A A A
F -> E B P
E -> F P
P -> B F E
B -> F P

'''


def dfs(node, destination, graph, visited):
    if node in visited:
        return
    visited.add(node)
    if node == destination:
        return
    for child in graph[node]:
        dfs(child, destination, graph, visited)


def path_exists(source, destination, graph):
    visited = set()
    dfs(source, destination, graph, visited)

    return destination in visited


for i in range(nodes):
    node, children_str = input().split(" -> ")
    children = children_str.split()
    graph[node] = children
    for child in children:
        edges.append((node, child))

#print(edges)

removed_edges = []

for source, destination in sorted(edges, key=lambda x: (x[0], x[1])):
    if destination not in graph[source] and source not in graph[destination]:
        continue
    graph[source].remove(destination)
    graph[destination].remove(source)

    if path_exists(source, destination, graph):
        #print(source, destination)
        removed_edges.append((source, destination))
    else:
        graph[source].append(destination)
        graph[destination].append(source)
        
print(f"Edges to remove: {len(removed_edges)}")
for first, second in removed_edges:
    print(f"{first} - {second}")