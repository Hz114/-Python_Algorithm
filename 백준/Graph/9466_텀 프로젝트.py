"""
재귀함수로 변경시 합격

"""

def BFS(graph, root):
    visit = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        if len(visit) != 0 and node == root:
            return visit, 1
        if node not in visit:
            queue.extend(graph[node])
            visit.append(node)

    return visit, 0

T = int(input())

for t in range(T):
    n = int(input())
    student = list(map(int, input().split()))

    graph = {}
    team = []
    visited = []

    for key in range(1, n+1):
        graph[key] = []
        graph[key].append(student[key-1])

        if key == student[key-1]:
            team.append(key)
            visited.append(key)

    for i in range(1, n+1):
        if i not in visited:
            visit, flag = BFS(graph, i)
            if flag:
                team.extend(visit)
                visited.extend(visit)
            else:
                visited.extend(visit)

    print(n-len(team))
