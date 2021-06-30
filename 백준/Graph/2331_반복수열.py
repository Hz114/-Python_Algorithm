A, P = map(int, input().split())

graph = {}
visited = []

node = A
count = 0

while True:
    next_node = 0
    for c in str(node):
        next_node += int(c) ** P

    if next_node not in graph:
        visited.append(node)
        graph[node] = set([next_node])
        node = next_node
    else:
        for i in range(len(visited)):
            if visited[i] == next_node:
                break
            else:
                count += 1
        break

print(count)