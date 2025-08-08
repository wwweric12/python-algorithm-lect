from collections import deque

n ,m = map(int,input().split())


lst=[[]for _ in range(n+1)]
res=[]
Q= deque()
ch=[0 for _ in range(n+1)]
for _ in range(m):
    a ,b =map(int,input().split())
    lst[a].append(b)
    ch[b]+=1

for i in range(1,n+1):
    if ch[i]==0:
        res.append(i)
        Q.append(lst[i])

while Q:
    tmp = Q.popleft()
    for i in tmp:
        ch[i]-=1
        if ch[i]==0:
            res.append(i)
            Q.append(lst[i])

for i in res:
    print(i, end=' ')


    
    
    
    
    