from collections import deque
n = int(input()) # 몇번할지

dx=[-1,1,-2,2,-2,2,-1,1]
dy=[-2,-2,-1,-1,1,1,2,2]

for _ in range(n): 
    l = int(input()) # 체스판 몇칸 
    sx,sy = map(int,input().split())
    ex,ey = map(int,input().split())
    Q= deque()
    Q.append((sx,sy))
    cnt=0
    state=True
    ch=[[0 for _ in range(l)] for _ in range(l)]
    if sx ==ex and sy == ey :
        state = False
    while state:
        size = len(Q)
        cnt+=1
        for i in range(size):
            x,y = Q.popleft()
            for j in range(8):
                xx=x+dx[j]
                yy=y+dy[j]
                if 0<=xx<l and 0<=yy<l and ch[yy][xx]==0:
                    ch[yy][xx]=1
                    Q.append((xx,yy))
                if xx == ex and yy == ey:
                    state=False
                    break
    print(cnt)
                
                    
        
    
    