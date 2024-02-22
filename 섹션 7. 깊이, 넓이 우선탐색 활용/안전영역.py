from collections import deque
n = int(input())
lst=[]
mv =0


Q= deque()
cnt=0
ch =[[0]*n for _ in range(n)]
res=0
dx=[-1,0,0,1]
dy=[0,-1,1,0]


for _ in range(n):
    tmp = list(map(int,input().split()))
    if mv < max(tmp):
        mv= max(tmp)
    lst.append(tmp)

for i in range(mv+1):
    for j in range(n):
        for k in range(n):
            if lst[j][k] <= i:
                ch[j][k]=1
    for a in range(n):
        for b in range(n):            
            if ch[a][b]==0:
                Q.append((a,b))
                ch[a][b]=1
                while Q:
                    tmp = Q.popleft()
                    for c in range(4):
                        xx=tmp[0]+dx[c]
                        yy=tmp[1]+dy[c]
                        if 0<= xx < n and 0<= yy < n and ch[xx][yy]==0:
                            ch[xx][yy]=1
                            Q.append((xx,yy))
                cnt+=1
    
                
    if res < cnt:
        res= cnt
    cnt=0
    ch =[[0]*n for _ in range(n)]

print(res)

#답안 
import sys
sys.setrecursionlimit(10**6) # 재귀함수일때 데이터같은게 많을때 이렇게 해야함

dx=[-1,0,0,1]
dy=[0,-1,1,0]

def DFS(x,y,h):
    ch[x][y]=1 # 체크
    for i in range(4):
        xx= x+dx[i]
        yy= y+dy[i]
        if 0 <= xx < n and 0<=yy < n and ch[xx][yy] == 0 and board[xx][yy] >h: 
            DFS(xx,yy,h)

if __name__ == "__main__":
    n = int(input())
    cnt =0
    res = 0
    board = [list(map(int,input().split())) for _ in range(n)]
    for h in range(100): 
        ch=[[0]*n for _ in range(n)]
        cnt=0
        for i in range(n):
            for j in range(n):
                if ch[i][j] == 0 and board[i][j] >h: # 안전지대(h보다 높은지역)을 만났을때
                    cnt+=1
                    DFS(i, j, h)
        res =max(res,cnt)
        if cnt == 0: # cnt가 0이라는것은 h보다 높은 안전지대가 없기때문에 break
            break 
    print(res)
        
    
