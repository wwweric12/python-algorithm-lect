import sys
from collections import deque

n, m = map(int,input().split())

y1, x1, y2, x2 = map(int,input().split())
x1-=1 
y1-=1
x2-=1
y2-=1
Q = deque([])
map=[]

for _ in range(n):
    map.append(list(input()))

dy = [-1,0,0,1]
dx = [0,1,-1,0]


res = 0
while True:
    res+=1
    Q.append((y1,x1))
    ch=[[0 for _ in range(m)] for _ in range(n)]
    ch[y1][x1] = 1
    while Q:
        y, x = Q.popleft()

        for i in range(4):
            yy = y + dy[i]
            xx = x + dx[i]
            if 0<=yy <n and 0<= xx < m:
                if x2 == xx and y2 == yy:
                    print(res)
                    sys.exit()
                    break
                elif map[yy][xx] == "1" and ch[yy][xx] ==0:
                    map[yy][xx] = "0" 
                    ch[yy][xx]  = 1
                elif map[yy][xx] == "0" and ch[yy][xx] ==0:
                    ch[yy][xx] = 1 
                    Q.append((yy,xx))
    

