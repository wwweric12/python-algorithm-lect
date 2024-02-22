from collections import deque

Q= deque()
n = int(input())

lst=[list(map(int,input().split()) )for _ in range(n)]
dx=[-1,-1,-1,0,0,1,1,1]
dy=[-1,0,1,-1,1,-1,0,1]

cnt=0
for i in range(n):
    for j in range(n):
        if lst[i][j]== 1:
            lst[i][j]=0
            Q.append((i,j))
            while Q:
                tmp = Q.popleft()
                for k in range(8):
                    xx= tmp[0] + dx[k]
                    yy = tmp[1] + dy[k]
                    if 0 <= xx < n and 0 <= yy <n and lst[xx][yy]==1:
                        Q.append((xx,yy))
                        lst[xx][yy]=0
                    
            cnt+=1

print(cnt)

#답안은 풀이와 동일




            
                    
                
            