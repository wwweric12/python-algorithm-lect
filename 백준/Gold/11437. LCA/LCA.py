import sys
input = sys.stdin.readline
N = int(input())

graph = [[] for _ in range(N+1)]
for i in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False]*(N+1)
visited[1] = True
LOG = N.bit_length()

parent = [[0 for _ in range(LOG)] for _ in range(N+1)] #
parent[1][0] = 1
level = [0]*(N+1)
stack = [1]
while stack:
    now = stack.pop()
    for i in graph[now]:
        if not visited[i]:
            visited[i] = True
            parent[i][0] = now
            level[i] = level[now] + 1
            stack.append(i)



for j in range(1,LOG):
    for i in range(1,N+1):
        parent[i][j] = parent[parent[i][j-1]][j-1]






M = int(input())
for i in range(M):
    a, b = map(int, input().split())
    if a == b:
        print(a)
        continue

    if level[a] > level[b]:
        diff = level[a] - level[b]
        for i in range(LOG):
            if diff & (1<<i):    
                a = parent[a][i]
    elif level[b] > level[a]:
        diff = level[b] - level[a]
        for i in range(LOG):
            if diff & (1<<i):    
                b = parent[b][i]
    if a == b:
        print(a)
        continue

    for i in range(LOG - 1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]

    print(parent[a][0])