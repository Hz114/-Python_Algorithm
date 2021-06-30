

K, N = map(int, input().split())

klist = []
left = 0
right = 0
mid = 0

for _ in range(K):
    k = int(input())
    right += k
    klist.append(k)

while (left < right):
    mid = (left + right) // 2
    if