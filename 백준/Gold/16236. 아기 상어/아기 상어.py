import sys
from collections import deque


n = int(input())
lst=[]

baby_shark=[]
result=0
dx=[-1,0,0,1]
dy=[0,-1,1,0]




for i in range(n):
    tmp =list(map(int,input().split()))
    for j in range(n):
        if tmp[j]==9:
            baby_shark=[i,j,2,0]
            tmp[j]=0
    lst.append(tmp)




def BFS():
    global baby_shark, result
    x,y,size,eaten = baby_shark
    Q=deque([(x,y,0)]) 
    ch=[[0 for _ in range(n)] for _ in range(n)]
    ch[x][y]=1
    candidates=[]
    while Q:
        x,y,dist = Q.popleft()
        if 0< lst[x][y]<size:
            candidates.append((dist,x,y))

        for i in range(4):
            xx= x+dx[i]
            yy= y+dy[i]
            if 0<= xx< n  and 0<=yy <n and lst[xx][yy] <= size and ch[xx][yy]==0 :
                ch[xx][yy]=1
                Q.append((xx,yy,dist+1,))
                
    if candidates:
        candidates.sort()  
        dist, nx, ny = candidates[0]
        result += dist
        lst[nx][ny] = 0  
        eaten += 1
        if eaten == size:
            size += 1
            eaten = 0
        baby_shark = [nx, ny, size, eaten]
        
        return True
    return False    
        

while True:
    if not BFS():
        break
print(result)
                
      

