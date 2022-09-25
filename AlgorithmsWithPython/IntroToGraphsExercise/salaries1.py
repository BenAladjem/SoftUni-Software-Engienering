nodes = int(input())
graph =[]
result = 0

'''
6
NNNNNN
YNYNNY
YNNNNY
NNNNNN
YNYNNN
YNNYNN

'''

for i in range(nodes):
    line = input()
    empl = []
    for j in range(len(line)):
        if line[j] == "Y":
            empl.append(j)
    graph.append(empl)
print(graph)

salaries = [None] * nodes


def dfs(node, graph, salaries):
    if salaries[node] is not None:
        return salaries[node]
    if len(graph[node]) == 0:
        salaries[node] = 1
        return 1

    salary = 0
    for el in graph[node]:
        salary += dfs(el, graph, salaries)
    return salary



for node in range(nodes):
    salaries[node] = dfs(node, graph, salaries)
    result += salaries[node]
print(salaries)
print(result)