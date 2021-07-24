from collections import deque

def BFS(box, ripe, maxNode):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    days = -1

    while ripe:
        days += 1
        for _ in range(len(ripe)):
            node = ripe.popleft()

            for i in range(4):
                nx = node[0] + dx[i]
                ny = node[1] + dy[i]

                if (0<=nx<maxNode[0] and 0<=ny<maxNode[1]) and (box[nx][ny]==0):
                    ripe.append([nx,ny])
                    box[nx][ny] = 1

    # 안익은 토마토가 있으면 -1
    for b in box:
        if 0 in b:
            return -1

    return days

M, N = map(int, input().split())

box = []
ripe = deque()

for n in range(N):
    row = list(map(int, input().split()))
    for m in range(M):
        if row[m] == 1:
            ripe.append([n,m])
    box.append(row)

days = BFS(box, ripe, [N,M])

print(days)