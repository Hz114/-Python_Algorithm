T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))

    check = [0 for _ in range(N)]
    check[M] = 1

    answer = 0
    while queue:
        q = queue[0]
        qCheck = check[0]

        if max(queue) == q:
            answer += 1
            del queue[0]
            del check[0]

            if qCheck:
                break
        else:
            queue.append(q)
            check.append(qCheck)
            del queue[0]
            del check[0]
    print(answer)






