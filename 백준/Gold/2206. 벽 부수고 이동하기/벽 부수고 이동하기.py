import sys
from collections  import deque

n, m = map(int,input().split())
Q=deque()
Q.append([0,0,1,1])
lst=[]
default_ch=[[0 for _ in range(m)] for _ in range(n)]
skill_ch=[[0 for _ in range(m)] for _ in range(n)]
default_ch[0][0]=1
skill_ch[0][0]=1
for _ in range(n):
    lst.append(list(map(int,input())))
    
dx=[0,1,-1,0]
dy=[-1,0,0,1]


while Q:
    x,y,cnt,skill=Q.popleft()
    if y==n-1 and x==m-1:
        print(cnt)
        sys.exit()
    else:
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<=yy<n and 0<=xx<m:
                if lst[yy][xx]==0 :
                    if skill==1 and default_ch[yy][xx]==0:
                        default_ch[yy][xx] = 1
                        Q.append([xx,yy,cnt+1,skill])
                    elif skill==0 and skill_ch[yy][xx]==0:
                        skill_ch[yy][xx]=1
                        Q.append([xx,yy,cnt+1,skill])  
                elif lst[yy][xx]==1 and skill==1 and skill_ch[yy][xx]==0:
                    skill_ch[yy][xx]=1  
                    Q.append([xx,yy,cnt+1,0])
            
print(-1)


