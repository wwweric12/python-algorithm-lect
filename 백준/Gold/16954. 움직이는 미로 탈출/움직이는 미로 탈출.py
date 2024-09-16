from collections import deque
import sys

lst=[]
for _ in range(8):
    lst.append(list(input()))
dy=[-1,-1,-1,0,0,0,1,1,1]
dx=[0,-1,1,0,-1,1,0,-1,1]
ch=[[0 for _ in range(8)] for _ in range(8)]
ch_stop=[[0 for _ in range(8)] for _ in range(8)]

Q=deque()
Q.append((7,0))


while Q:
    x, y=Q.popleft()
    if x==0:
        print(1)
        sys.exit()
    for i in range(8):
        xx= x+dx[i]
        yy= y+dy[i]
        if 0<=xx<8 and 0<=yy<8 and lst[xx][yy]=="." and lst[xx-1][yy]=="." and ch[xx][yy]==0:
            ch[xx][yy]=1
            Q.append((xx-1,yy))
            if ch_stop[xx][yy]==0:
                ch_stop[xx][yy]=1
                Q.append((xx,yy))
            
print(0)



