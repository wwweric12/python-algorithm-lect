import sys
from collections import deque

input = sys.stdin.readline
n,m = map(int,input().split())

ch=[0]*(n+1)
lst=[[] for _ in range(n+1)]

for i in range(m):
    a,b =list(map(int,input().split()))
    lst[a].append(b)
    lst[b].append(a)

Q=deque()
cnt=0
for i in range(1,n+1):
    Q.append(i)
    if ch[i]==0:    
        ch[i]=1
        while Q:
            tmp=Q.popleft()
            for j in lst[tmp]:
                if ch[j] ==0:
                    ch[j]=1
                    Q.append(j)
        cnt+=1
    else:
        Q.popleft()
        
            
print(cnt)
        



    





