from collections import deque

def BFS(graph, root):
    visit = []
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])

    return visit

N, M = map(int, input().split())

graph = {}

for key in range(1, N+1):
    graph[key] = set()

for _ in range(M):
    u, v = map(int, input().split())

    graph[u].add(v)
    graph[v].add(u)

count = 0
visit = []
for node in range(1, N+1):
    if node not in visit:
        visit.extend(BFS(graph, node))
        count +=1

print(count)

'''
# 시간초과
# set연산은 시간이 오래걸린다

for node in range(1, N+1):
    # 집합의 연산을 이용하기 위해서 set으로 visit의 값을 저장
    dfs_visit = set(BFS(graph, node))

    # set사이 -는 차집합 dfs_visit와 visit사이 다른 값이 생기면 0([])이상의 set을 return
    if dfs_visit - visit:
        # set사이 |는 합집합 dfs_visit와 visit의 모든 값을 합한 set이 return
        visit = visit | dfs_visit
        count += 1

print(count)
'''