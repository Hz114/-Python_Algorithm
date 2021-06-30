def BFS(graph, root):
    visit = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])

    return visit

V = int(input())
E = int(input())

graph ={}
for key in range(1, V+1):
    graph[key] = []

for _ in range(E):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

visit = BFS(graph, 1)
print(len(visit) - 1)