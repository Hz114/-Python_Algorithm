'''
인접리스트 구현
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
adj = {}

# 양방향 그래프 (Undirected Graph)
un_adj = {}

for key in range(1,V+1):
    adj[key] = []
    un_adj[key] = []


for _ in range(E):
    i, j = map(int,input().split())

    # 단방향 그래프 (directed Graph)
    adj[i].append(j)

    # 양방향 그래프 (Undirected Graph)
    un_adj[i].append(j)
    un_adj[j].append(i)


print('단방향 그래프')
print(adj)

print('\n양방향 그래프')
print(un_adj)
