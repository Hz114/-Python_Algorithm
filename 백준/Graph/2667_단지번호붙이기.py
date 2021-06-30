def BFS(maps, visit, N, x, y, answer):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    queue = []
    queue.append((x, y))
    maps[x][y] = answer
    visit[x][y] = 1
    cnt = 1

    while queue:
        node = queue.pop(0)
        for i in range(4):
            nx = node[0] + dx[i]
            ny = node[1] + dy[i]
            if (0 <= nx < N and 0 <= ny < N) and (maps[nx][ny] == 1 and visit[nx][ny] == 0):
                queue.append([nx, ny])
                maps[nx][ny] = answer
                visit[nx][ny] = 1
                cnt += 1

    return maps, visit, cnt


N = int(input())
maps = []
visit = [[0 for row in range(N)] for col in range(N)]
for col in range(N):
    row = list(map(int, input()))
    maps.append(row)

answer = 0
answerList = []
for col in range(N):
    for row in range(N):
        if maps[col][row] == 1 and visit[col][row] == 0:
            answer += 1
            maps, visit, cnt = BFS(maps, visit, N, col, row, answer)
            answerList.append(cnt)

print(answer)
answerList.sort()
for i in range(len(answerList)):
    print(answerList[i])

