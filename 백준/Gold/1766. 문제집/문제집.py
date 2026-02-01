import sys
import heapq 


input = sys.stdin.readline

n, m = map(int,input().split())

ch=[0 for _ in range(n+1)] ## 끝났는지 
cnt= [0 for _ in range(n+1)] ## 몇개 남았는지
start = [[] for _ in range(n+1)] ##


for _ in range(m):
    before, after = map(int,input().split())
    heapq.heappush(start[before],after)
    cnt[after] += 1

Q=[]

for i in range(1,n+1):
    if cnt[i] == 0:
        heapq.heappush(Q,i)

res=[]
while Q:
    node = heapq.heappop(Q)
    res.append(node)
    for i in start[node]:
        cnt[i] -=1
        if cnt[i] == 0:
            heapq.heappush(Q,i)


for i in res:
    print(i, end=' ')


