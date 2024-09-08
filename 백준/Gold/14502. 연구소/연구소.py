from collections import deque
n, m =map(int,input().split())
lst=[]
virus=[]
safe=0
for i in range(n):
    tmp=list(map(int,input().split()))
    for j in range(m):
        if tmp[j]==2:
            virus.append([i,j])
        elif tmp[j]==0:
            safe+=1
    lst.append(tmp)
            
max_value=0
dy=[-1,0,0,1]
dx=[0,1,-1,0]



def wall(L,start):
    if L ==3:
        global safe, max_value
        cp_lst=[row[:] for row in lst]
        Q=deque()
        for v in virus:
            Q.append(v)
        cp_safe= safe-3
        while Q:
            x,y=Q.popleft()
            for i in range(4):
                xx=x+dx[i]
                yy=y+dy[i]
                if 0<=xx<n and 0<=yy<m and cp_lst[xx][yy]==0:
                    Q.append([xx,yy])
                    cp_lst[xx][yy]=2
                    cp_safe-=1
            if max_value >= cp_safe:
                return
        max_value= max(max_value,cp_safe)
        return 
    else:
        for i in range(start,n*m):
            x= i//m
            y=i%m
            if lst[x][y]==0:
                lst[x][y]=1
                wall(L+1,i+1)
                lst[x][y]=0
        
wall(0,0)
print(max_value)