from collections import deque
    
n=int(input())
lst=[list(map(int,input()))for _ in range(n)]
dx = [-1,0,0,1]
dy = [0,1,-1,0]
res=[]
Q =deque()
for i in range(n):
    for j in range(n):
        if lst[i][j] == 1:
            Q.append((i,j))
            lst[i][j]=0
            cnt=1
            while Q:
                tmp = Q.popleft()
                for k in range(4):
                    xx = tmp[0] + dx[k]
                    yy = tmp[1] + dy[k]
                    if 0<=xx<n and 0<=yy<n and lst[xx][yy] == 1:
                        Q.append((xx,yy))       
                        lst[xx][yy]=0
                        cnt+=1
            res.append(cnt)

print(len(res))
res.sort()
for i in res:
    print(i)
    
    
#답안

dx = [-1,0,0,1]
dy = [0,1,-1,0]

def DFS(x, y):
    global cnt
    cnt+=1
    board[x][y]=0
    for i in range(4):
        xx= x+dx[i]
        yy= y+dy[i]
        if 0<=xx<n and 0<=yy<n and board[xx][yy] == 1:
            DFS(xx, yy)


if __name__ == "__main__":
    n= int(input())
    board =[list(map(int,input()))for _ in range(n)]
    res=[]
    for i in range(n):
        for j in range(n):
            if board[i][j]==1:
                cnt=0
                DFS(i,j)
                res.append(cnt)

print(len(res))
res.sort()
for x in res:
    print(x)
