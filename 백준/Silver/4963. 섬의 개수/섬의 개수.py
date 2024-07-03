from collections import deque
import sys
input = sys.stdin.readline

Q=deque()
dx=[1,1,1,0,0,-1,-1,-1]
dy=[0,1,-1,1,-1,-1,0,1]
res=[]
while True:
    w,h = map(int,input().split())
    cnt=0
    lst=[]
    ch=[[0 for _ in range(w)] for _ in range(h)]
    if w==0 and h==0:
        break
    else:
        for _ in range(h):
            tmp=list(map(int,input().split()))
            lst.append(tmp)

        for i in range(h):
            for j in range(w):    
                if lst[i][j]==1 and ch[i][j]==0:
                    Q.append((i,j))
                    ch[i][j]=1
                    while Q:
                        size =len(Q)
                        for a in range(size):
                            x,y =Q.popleft()
                            for k in range(8):
                                xx=x+dx[k]
                                yy=y+dy[k]
                                if  0<=xx<h and 0<=yy<w and lst[xx][yy]==1 and ch[xx][yy]==0 :
                                    Q.append((xx,yy))
                                    ch[xx][yy]=1
                    cnt+=1
    print(cnt)
              

      
                            
                                            
        
          
    