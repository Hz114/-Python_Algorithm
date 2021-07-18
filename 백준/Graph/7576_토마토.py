def BFS(maps, rootNode, maxNode, visit):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    visit[rootNode[0]][rootNode[1]] = 1
    queue = [rootNode]

    days = 0

    while queue:
        node = queue.pop(0)
        flag = False
        for i in range(4):
            nx = node[0] + dx[i]
            ny = node[1] + dy[i]

            if (0<=nx<=maxNode[0] and 0<=ny<=maxNode[1]) and (maps[nx][ny]==0 and visit[nx][ny]==0):
                queue.append([nx,ny])
                visit[nx][ny] = 1
                flag = True

        if flag:
            days += 1

    return visit, days

M, N = map(int, input().split())

visited = [[0 for row in range(M)] for col in range(N)]
maps = []
for _ in range(N):
    n = list(map(int, input().split()))
    maps.append(n)

result = 0
for col in range(N):
    for row in range(M):
        if maps[col][row] == 1:
            visited, days = BFS(maps, [col, row], [N-1, M-1], visited)
            result += days

print(result)




print(maps)
print(visited)