from collections import deque 
n, k, r = map(int,input().split())

board=[[0 for _ in range(n)] for _ in range(n)]

graph=[[[0 for _ in range(4)] for _ in range(n)] for _ in range(n)]


dx=[-1,0,1,0]
dy=[0,1,0,-1]
## 1:위, 2:오른쪽, 3:아래, 4:왼쪽

for _ in range(r):
    x1,y1,x2,y2 = map(int,input().split())
    x1-=1
    y1-=1
    x2-=1
    y2-=1
    if x1==x2+1:
        graph[x1][y1][0]=1
        graph[x2][y2][2]=1
    elif x1==x2-1:
        graph[x1][y1][2]=1
        graph[x2][y2][0]=1
    
    elif y1==y2+1:
        graph[x1][y1][3]=1
        graph[x2][y2][1]=1
    elif y1==y2-1:
        graph[x1][y1][1]=1
        graph[x2][y2][3]=1
        

cows=[]

res=0 


for _ in range(k):
    x,y =map(int,input().split())
    board[x-1][y-1] = 1
    cows.append((x-1,y-1))


Q=deque([])

group=[[0 for _ in range(n)] for _ in range(n)]

cow_lst=[]

for i in range(n):
    for j in range(n):
        if group[i][j] == 0:
            Q.append((i,j))
            group[i][j]=1
            cnt=0
            if board[i][j] == 1:
                cnt+=1
            while Q:
                x,y  = Q.popleft()
                for j in range(4):
                    if graph[x][y][j]==0:
                        xx= x + dx[j]
                        yy= y + dy[j]
                        if 0<=xx<n and 0<=yy<n  and group[xx][yy]==0:
                            if board[xx][yy]==1:
                                cnt+=1
                            group[xx][yy]=1
                            Q.append((xx,yy))
            cow_lst.append(cnt)


for i in range(len(cow_lst)-1):
    for j in range(i+1,len(cow_lst)):          
        res+=cow_lst[i]*cow_lst[j]

print(res)