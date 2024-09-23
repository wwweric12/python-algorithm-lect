import sys
from collections import deque

input = sys.stdin.readline
w, h = map(int,input().split())

lst=[]
razer=[]

dx=[0,1,0,-1]  # 왼 아래 0,1,2,3
dy=[-1,0,1,0]
ch=[[10000 for _ in range(w)] for _ in range(h)]

for i in range(h):
    tmp =list(input().strip())
    for j in range(w):
        if tmp[j] == "C":
            razer.append((i,j,-1,0))
    lst.append(tmp)
            
Q=deque()
Q.append(razer[0])
ch[razer[0][0]][razer[0][1]]=0

while Q:
    x, y, direction,cnt = Q.popleft()
    for i in range(4):
        xx = x
        yy = y
        while True:
            xx+=dx[i]
            yy+=dy[i]
            if not (0<= xx <h and 0<= yy <w) :
                break
            if lst[xx][yy]== "*":
                break
            if direction == -1 or direction == i:
                if ch[xx][yy] > cnt:
                    ch[xx][yy] = cnt
                    Q.append((xx, yy, i, cnt))
            else:
                if ch[xx][yy] > cnt + 1:
                    ch[xx][yy] = cnt + 1
                    Q.append((xx, yy, i, cnt + 1))



print(ch[razer[1][0]][razer[1][1]])


