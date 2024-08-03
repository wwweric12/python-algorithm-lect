from collections import deque

n , m = map(int,input().split())
lst=[]
for _ in range(m):
    lst.append(list(map(int,input())))
ch=[[1000000 for _ in range(n)]for _ in range(m)]

dy=[-1,0,0,1]
dx=[0,1,-1,0]
ch[0][0]=0
Q = deque()
Q.append((0,0,0))

while Q:
    x, y, cnt=Q.popleft()
    if x== n-1 and y==m-1:
        print(ch[y][x])
        break
        
    else:
        for i in range(4):
            xx =x+dx[i]
            yy = y+dy[i]
            if 0<= xx <n and 0<=yy <m:
                if lst[yy][xx]==0 and ch[yy][xx] > cnt:
                    ch[yy][xx]=cnt
                    Q.appendleft((xx,yy,cnt))
                elif lst[yy][xx]==1 and ch[yy][xx] > cnt+1:
                    ch[yy][xx]=cnt+1
                    Q.append((xx,yy,cnt+1))



            



    