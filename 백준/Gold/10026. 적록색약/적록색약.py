from collections import deque

n= int(input())
lst=[]
for _  in range(n):
    tmp=list(input().strip())
    lst.append(tmp)
    


ch=[ [0 for _ in range(n)] for _ in range(n)]


dy=[-1,0,0,1]
dx=[0,1,-1,0]



def BFS(x,y,color,state):
    Q=deque()
    Q.append((x,y))
    ch[x][y]=1
    while Q:
        x,y=Q.popleft()
        for i in range(4):
            xx= x+dx[i]
            yy= y+dy[i]
            if 0<=xx<n and 0<=yy<n and ch[xx][yy]==0:
                if state ==1:
                    if (color=="R" or color =="G" ) and (lst[xx][yy]=="R" or lst[xx][yy]=="G"):
                        ch[xx][yy]=1
                        Q.append((xx,yy))
                    elif color==lst[xx][yy] :
                        ch[xx][yy]=1
                        Q.append((xx,yy))
                else:
                    if color == lst[xx][yy]:
                        ch[xx][yy]=1
                        Q.append((xx,yy))


                
group_cnt =0
group_color_cnt =0

for i in range(n):
    for j in range(n):
        if ch[i][j]==0:
            BFS(i,j,lst[i][j],0)
            group_cnt+=1
            
ch=[ [0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if ch[i][j]==0:
            BFS(i,j,lst[i][j],1)
            group_color_cnt+=1
    
print(group_cnt,group_color_cnt)