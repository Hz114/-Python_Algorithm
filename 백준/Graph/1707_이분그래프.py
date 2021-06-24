from collections import deque

def BFS(graph, root):
    queue = deque([root])
    visited = []
    bg = [0 for _ in range(len(graph)+1)]

    bg[root] = 1
    flag = False

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])

            # bg리스트에서 node의 값이 1이면 node와 연결 된 값(n)은 -1으로 표시
            for n in graph[node]:
                # flag가 True인 경우 이분그래프가 아님
                if flag:
                    break;

                # bg리스트에서 node와 node와 연결된 값(n)이 같은 경우는 이분그래프가 아님
                if bg[n] == bg[node]:
                    flag = True
                else:
                    bg[n] = -1 * bg[node]

    return visited, flag

K = int(input())

for _ in range(K):
    V, E = map(int, input().split())

    graph = {}

    for key in range(1, V+1):
        graph[key] = set()

    for _ in range(E):
        u, v = map(int, input().split())

        graph[u].add(v)
        graph[v].add(u)

    # 비연결 그래프 가능성이 존재 모든 노드에 대해서 확인
    visited = []
    flag = False
    for node in range(1, V+1):
        if node not in visited:
            visit, flag = BFS(graph, node)
            visited.extend(visit)

            if flag:
                break

    # flag가 True면 이분 그래프가 아님 / False면 이분 그래프
    if flag:
        print('NO')
    else:
        print('YES')