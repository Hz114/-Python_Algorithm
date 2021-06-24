def DFS(graph, root):
    visit = []
    stack = [root]

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])

    return visit

T = int(input())

for _ in range(T):
    N = int(input())
    plist = list(map(int, input().split()))

    graph = {}
    for key in range(1, N+1):
        graph[key] = set()

    for node in range(1, N+1):
        graph[node].add(plist[node-1])

    count = 0
    visited = []

    for node in range(1, N+1):
        if node not in visited:
            visited.extend(DFS(graph, node))
            count += 1

    print(count)

