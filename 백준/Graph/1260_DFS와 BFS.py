from collections import deque

def DFS(graph, root):
    visit =[]
    stack = [root]

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            # 오름차순으로 스택을 쌓아서 작은 숫자 먼저 탐색
            stack.extend(reversed(list(graph[node])))
            print(node, end=" ")

def BFS(graph, root):
    visit = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])
            print(node, end=" ")

V, E, root = map(int, input().split())

graph = {}

for key in range(1, V+1):
    graph[key] = set()

for _ in range(E):
    i, j = map(int, input().split())

    graph[i].add(j)
    graph[j].add(i)


# 입력된 값을 내림차 순으로 변경
for key in range(1, V+1):
    graph[key] = sorted(graph[key])

DFS(graph, root)
print()
BFS(graph, root)
