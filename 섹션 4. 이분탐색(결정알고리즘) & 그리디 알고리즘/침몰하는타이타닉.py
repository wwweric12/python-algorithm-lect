n, m = map(int,input().split())

lst=list(map(int,input().split()))


lst.sort()
cnt=0
lt =0
rt= n-1

while lt<=rt:
    if lst[lt]+lst[rt]<=m:
        cnt+=1
        lt+=1
        rt-=1
    else:
        cnt+=1
        rt-=1
    
    
print(cnt)

#답안

n, limit = map(int,input().split())

p=list(map(int,input().split()))

p.sort()
cnt=0

while p:
    if len(p) ==1:
        cnt+=1
        break
    if p[0]+p[-1]>limit:
        p.pop()
        cnt+=1
    else:
        p.pop(0)
        p.pop()
        cnt+=1
print(cnt)

# deque
# list에서 빼는것이아니라 가리키는것을 옮기는 자료구조 
from collections import deque

n, limit = map(int,input().split())

p=list(map(int,input().split()))
p.sort()
p=deque(p)

while p:
    if len(p) ==1:
        cnt+=1
        break
    if p[0]+p[-1]>limit:
        p.pop()
        cnt+=1
    else:
        p.popleft()
        p.pop()
        cnt+=1
print(cnt)