import sys
from collections import deque


n,m,k = map(int,input().split())
lst=[]
Q=deque()
Q.append((0,0,k))

dx=[-1,0,0,1]
dy=[0,1,-1,0]

for _ in range(n):
    lst.append(list(map(int,input())))
    
ch=[[[0 for _ in range(m)] for _ in range(n)]for _ in range(k+1)]
for i in range(k):
    ch[i][0][0]=1


while Q:
    x,y,skill =Q.popleft()
    if x==n-1 and y==m-1 :
        print(ch[skill][x][y]+1)
        sys.exit()
    else:
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<=xx<n and 0<=yy<m:
                if lst[xx][yy]==1 and skill!=0 and ch[skill-1][xx][yy]==0:
                    ch[skill-1][xx][yy]=ch[skill][x][y]+1
                    Q.append((xx,yy,skill-1))
                elif lst[xx][yy]==0 and ch[skill][xx][yy]==0:
                    ch[skill][xx][yy]=ch[skill][x][y]+1
                    Q.append((xx,yy,skill)) 
                    
                

print(-1)


