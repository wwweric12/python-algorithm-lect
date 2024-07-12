import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
ch=[[0 for _ in range(n+1)]for _ in range(n+1)]
for i in range(n):
    a ,b = map(int,input().split()) 
    ch[a][b]=1 # 바로옆이면 거리 1로 표현 
    ch[b][a]=1 # 반대도 마찬가지

visited=[]            # 순환되는것 찾으려고 
state=False # 순환되는것을 찾으면 False로 더이상 로직 수행 안하도록 
circle=[]
def DFS(L,I,k,prev):
    global state,circle
    if L==n+1 or state : # n+1번이면 모든 거리를 다 알 수 있기때문에 n+1로 설정 
        return
    else:
        for v in range(1,n+1): 
            if ch[I][v]==1 and v!=prev: # ch[I][v]==1 은 거리가 1인(바로옆에있는역)을 찾으려고 이전에 왔던거랑 같으면 안되니깐 prev랑 다르게 설정 
                if v not in visited: 
                    visited.append(v)
                    DFS(L+1,v,k,I) 
                    visited.pop()
                elif v in visited and state==False: # 만약 바로전에 방문하지않았는데 이미 방문한곳이면 순환
                    state=True
                    idx=visited.index(v) # v에서 지금 지점까지 순환이기때문에 그전에 방문지점 삭제
                    circle=visited[idx::] ## 최종 순환 
                    return 



for i in range(1,n+1):
    if state:
        break
    visited.append(i)
    DFS(1,i,i,0)
    visited.pop()

def BFS():
        
    Q= deque()
    for i in circle:
        res[i]=0
        Q.append(i)
    while Q:
        now =Q.popleft()
        for i in range(1,n+1):
            if ch[now][i]==1 and res[i]==-1:
                Q.append(i)
                res[i]=res[now]+1
        
                
        
res=[-1 for _ in range(n+1)]
BFS()

for i in range(1,n+1):
    print(res[i],end=' ')
       
    
    
    