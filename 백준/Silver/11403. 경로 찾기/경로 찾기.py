from collections import deque

n = int(input())

ch=[]
res=[[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    tmp = list(map(int,input().split()))
    ch.append(tmp)
    

Q=deque()
for i in range(n):
    for j in range(n):
        if ch[i][j]==1:
            Q.append((i,j))
            res[i][j]=1


while Q:
   start,end =Q.popleft()
   for k in range(n):
       if ch[end][k] == 1 and res[start][k]==0:
            res[start][k]=1
            Q.append((start,k))



for i in range(n):
    for j in range(n):
        print(res[i][j],end=" ")
    print()