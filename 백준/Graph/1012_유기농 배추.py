def BFS(maps, visit, N, M, x, y):
    queue = [(x, y)]
    visit[x][y] = 1

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while queue:
        node = queue.pop(0)
        for i in range(4):
            nx = node[0] + dx[i]
            ny = node[1] + dy[i]

            if (0 <= nx < M and 0 <= ny < N) and (maps[nx][ny] == 1 and visit[nx][ny] == 0):
                queue.append((nx,ny))
                visit[nx][ny] = 1

    return visit

T = int(input())
for t in range(T):
    M, N, K = map(int, input().split())

    maps = [[0 for n in range(N)] for m in range(M)]
    visit = [[0 for n in range(N)] for m in range(M)]

    for k in range(K):
        X, Y = map(int, input().split())
        maps[X][Y] = 1

    answer = 0
    for col in range(M):
        for row in range(N):
            if maps[col][row] == 1 and visit[col][row] == 0:
                visit = BFS(maps, visit, N, M, col, row)
                answer += 1

    print(answer)