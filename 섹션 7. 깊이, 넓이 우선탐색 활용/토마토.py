from collections import deque
m, n = map(int,input().split())

lst= [list(map(int,input().split())) for _ in range(n)]
res=0
Q = deque()
dx=[-1,0,0,1]
dy=[0,1,-1,0]
t=0

for i in range(n):
    for j in range(m):
        if lst[i][j] == 1:
            Q.append((i,j))
        elif lst[i][j] ==0:
            t+=1
            

while Q and t>0:
    res+=1
    for _ in range(len(Q)): # 이렇게 하면 이전의 len(Q)값만 가지고 for 문을 돌릴 수 있다 
        tmp = Q.popleft()
        for k in range(4):
            xx = tmp[0]+dx[k]
            yy = tmp[1]+dy[k]
            if 0 <= xx < n and 0 <= yy < m and lst[xx][yy] ==0 :
                lst[xx][yy] =1
                Q.append((xx,yy))
                t-=1

if t >0:
    print(-1)
else:
    print(res)



#답안


from collections import deque
n, m = map(int,input().split())
board= [list(map(int,input().split())) for _ in range(m)]   
Q = deque()
dx=[-1,0,0,1]
dy=[0,1,-1,0]
dis= [[0]*n for _ in range(m)]

for i in range(m):
    for j in range(n):
        if board[i][j] == 1:
            Q.append((i,j))
while Q:
    tmp= Q.popleft()
    for i in range(4):
        xx = tmp[0]+dx[i]
        yy = tmp[1]+dy[i]
        if 0<= xx < m and  0<= yy < n and board[xx][yy]==0:
            board[xx][yy]=1
            dis[xx][yy]=dis[tmp[0]][tmp[1]]+1 #부모지점에서 +1 해주는거임 
            Q.append((xx,yy))

flag =1 

for i in range(m): # 다 끝나고 board에 0이 남아있는경우
    for j in range(n):
        if board[i][j] == 0 :
            flag=0
result=0

if flag == 1:
    for i in range(m): 
        for j in range(n):
            if dis[i][j] > result:
                result = dis[i][j]
    print(result)
else:
    print(-1)