N, M = map(int, input().split())
r, c, d = map(int, input().split())
# 0 위(북쪽) U, 1 왼쪽(동쪽) L, 2 아래(남쪽) D, 3 오른쪽(서쪽) R

home = [list(map(int, input().split())) for _ in range(N)]
'''
for _ in range(N):
    row = list(map(int, input().split()))
    home.append(row)
'''
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
# 북 동 남 서

c = 0
while True:
    if not home[r][c]:
        c += 1
        home[r][c] = 2

print(home)