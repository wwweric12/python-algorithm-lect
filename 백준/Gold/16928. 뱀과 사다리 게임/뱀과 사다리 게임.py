from collections import deque

n,m =map(int,input().split())

lst=[0 for _ in range(101)]
ch=[101 for _ in range(101)]


for _ in range(n+m):
    a, b = map(int,input().split())
    lst[a]=b

Q= deque()

Q.append([1,0])
ch[1]=0

while Q:
    loc, cnt=Q.popleft()
    for i in range(1,7):
        if loc+i <101 and ch[loc+i]>cnt+1:
            if lst[loc+i]!=0 and ch[lst[loc+i]] > cnt+1 :
                ch[lst[loc+i]] = cnt + 1 
                Q.append([lst[loc+i],cnt+1])
            elif lst[loc+i]==0:
                ch[loc+i]=cnt+1
                Q.append([loc+i,cnt+1])


            
print(ch[100])     
        
        










