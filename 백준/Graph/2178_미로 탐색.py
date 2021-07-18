def DFS(maps, visit, maxNode, rootNode):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    queue = [rootNode]
    visit[rootNode[0]][rootNode[1]] = 1

    while queue:
        node = queue.pop(0)
        for i in range(4):
            nx = node[0] + dx[i]
            ny = node[1] + dy[i]
            if (0 <= nx < maxNode[0] and 0 <= ny < maxNode[1]) and (maps[nx][ny] == 1 and visit[nx][ny] == 0):
                queue.append([nx,ny])
                visit[nx][ny] = visit[node[0]][node[1]] + 1
    return visit

N, M = map(int, input().split())

visit = [[0 for m in range(M)] for n in range(N)]

maps = []
for n in range(N):
    m = list(map(int, input()))
    maps.append(m)

visited = DFS(maps, visit, [N, M], [0, 0])
# print(visited)
print(visited[N-1][M-1])