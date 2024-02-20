import sys
from collections import deque
lst=[]
for _ in range(7):
    lst.append(list(map(int,input().split())))
dx=[-1,0,0,1]
dy=[0,1,-1,0]
Q=deque()
Q.append((0,0))
cnt=0
ch=[[1]*7 for _ in range(7)]
while True:
    size =len(Q)
    for j in range(size):
        tmp = Q.popleft()
        if tmp == (6,6):
            print(cnt)
            sys.exit()
        for i in range(4):
            x= tmp[0]+dx[i]
            y= tmp[1]+dy[i]
            if 0<=x<=6 and 0<= y <=6 and lst[x][y] == 0 and ch[x][y] == 1 :
                Q.append((x,y))
                ch[x][y]=0

    if len(Q)==0:
        print(-1)
        sys.exit()
    cnt+=1
    
            
#답안

import sys
from collections import deque


board=[list(map(int,input().split())) for _ in range(7)]
dx=[-1,0,1,0]
dy=[0,1,0,-1]
Q=deque()
Q.append((0,0))
cnt=0
board[0][0]=1
dis=[[0]*7 for _ in range(7)]
while Q: # Q가 비어있으면 종료
    tmp = Q.popleft()
    for i in range(4):
        x= tmp[0]+dx[i]
        y= tmp[1]+dy[i]
        if 0<=x<=6 and 0<= y <=6 and board[x][y] == 0 :
            board[x][y]=1 #갔던곳 체크
            dis[x][y] = dis[tmp[0]][tmp[1]]+1 # 몇번만에 갔는지 체크
            Q.append((x,y))

if dis[6][6]==0: # 값이 0이라는것은 가지 못했다는것 이기때문에 -1 출력 
    print(-1)
else:
    print(dis[6][6])
    
            

