'''
인접행렬 구현
V = 노드의 갯수
E = 간선의 갯수

E개의 줄에 걸쳐서 연결된 노드를 표현
i에서 j로 가는 간선이 존재

'''

'''
Test case
4 5
1 2
1 3
1 4
2 3
3 4
'''


V, E = map(int, input().split())

# 단방향 그래프 (directed Graph)
adj = [[0 for col in range(V)] for row in range(V)]

# 양방향 그래프 (Undirected Graph)
un_adj = [[0 for col in range(V)] for row in range(V)]

for _ in range(0, E):
    i, j = map(int, input().split())

    # 단방향 그래프 (directed Graph)
    adj[i-1][j-1] = 1

    # 양방향 그래프 (Undirected Graph)
    un_adj[i-1][j-1] = 1
    un_adj[j-1][i-1] = 1

print('단방향 그래프')
print(*adj, sep="\n")

print('\n양방향 그래프')
print(*un_adj, sep="\n")



