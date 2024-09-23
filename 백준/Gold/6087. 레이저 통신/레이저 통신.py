import sys
from collections import deque

input = sys.stdin.readline
w, h = map(int,input().split())

lst=[]
razer=[]

dx=[0,1,0,-1]  # 왼 아래 0,1,2,3
dy=[-1,0,1,0]
ch = [[[10000 for _ in range(4)] for _ in range(w)] for _ in range(h)]

for i in range(h):
    tmp =list(input().strip())
    for j in range(w):
        if tmp[j] == "C":
            razer.append((i,j))
    lst.append(tmp)
            
Q=deque()

for i in range(4):
    ch[razer[0][0]][razer[0][1]][i]=0
    Q.append((razer[0][0],razer[0][1],i,0))

while Q:
    x, y, direction,cnt = Q.popleft()
  
    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]
        if 0<= xx <h and 0<= yy <w and lst[xx][yy]!= "*":
            if  direction == i :
                if ch[xx][yy][i]>cnt  :
                    ch[xx][yy][i]= cnt
                    Q.appendleft((xx,yy,i,cnt))
            elif  direction != i and  ch[xx][yy][i]>cnt+1 :
                ch[xx][yy][i]= cnt+1
                Q.append((xx,yy,i,cnt+1))
    



print(min(ch[razer[1][0]][razer[1][1]]))


