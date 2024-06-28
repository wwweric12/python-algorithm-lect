from collections import deque
import sys
input = sys.stdin.readline

n,m,v = map(int,input().split())
dfs_res=[]
ch=[[] for _ in range(n+1)]
for i in range(m):
    a,b= list(map(int,input().split()))
    ch[a].append(b)
    ch[b].append(a)

dfs_ch=[0]*(n+1)
dfs_state=False

for j in ch:
    j.sort()



def DFS(v):
    dfs_ch[v] = True
    print(v, end=' ')
    for i in ch[v]:
        if not dfs_ch[i]:
            DFS(i)

DFS(v)
print()
        
        
bfs_ch=[0]*(n+1)
bfs_res=[]

Q=deque([v])
while Q:
    tmp =  Q.popleft()
    if bfs_ch[tmp] == 0:
        bfs_ch[tmp]=1
        bfs_res.append(tmp)
        for i in ch[tmp]:
            Q.append(i)
    

for i in bfs_res:
    print(i,end=' ')
    
    
    