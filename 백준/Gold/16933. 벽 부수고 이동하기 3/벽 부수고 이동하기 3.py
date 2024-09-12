import sys 
from collections import deque
n,m,k =map(int,input().split())
lst=[]
for _ in range(n):
    lst.append(list(map(int,input())))

ch=[[[0 for _ in range(m)] for _ in range(n)] for _ in range(k+1)]
dx=[-1,0,0,1]
dy=[0,1,-1,0]


Q=deque()
Q.append((0,0,k,1))
ch[k][0][0]=1

while Q:
    x,y,skill,ans=Q.popleft()
    if x== n-1 and y == m-1:
        print(ans)
        sys.exit()
    else:
        time =ans%2
        for i in range(4):
            xx= x+dx[i]
            yy= y+dy[i]
            if 0<=xx< n and 0<=yy<m:
                if lst[xx][yy]==0 and ch[skill][xx][yy]==0:
                    ch[skill][xx][yy]=ans
                    Q.append((xx,yy,skill,ans+1))
                elif lst[xx][yy]==1 and  skill>0  and ch[skill-1][xx][yy]==0:
                    if time :
                        ch[skill-1][xx][yy]=ans
                        Q.append((xx,yy,skill-1,ans+1))
                    else  :
                        Q.append((x,y,skill,ans+1))
                       
                        
                    
                    
                
print(-1)

