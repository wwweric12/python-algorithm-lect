import sys
sys.setrecursionlimit(1000000)

from collections import deque

Q=deque([])


n = int(input())

graph = [[] for _ in range(n+1)]


ch=[0 for _ in range(n+1)]
for _ in range(n-1):
    a ,b =map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    ch[a]+=1
    ch[b]+=1

visited=[0 for _ in range(n+1)]

leaf = 0
for i in range(1,n+1):
    if ch[i] == 1 :
        leaf =i
        visited[i]=1
        break

max_length = 0
max_node = 0    

def DFS(L,node):
    global max_length,max_node
    if L > max_length:
        max_length = L
        max_node = node
    for parent in graph[node]:
        if visited[parent] ==0:
            visited[parent]=1
            DFS(L+1,parent)


DFS(0,leaf)
visited=[0 for _ in range(n+1)]
DFS(0,max_node)

print((max_length+1)//2)

            
            
    

