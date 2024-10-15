import heapq
import sys
input= sys.stdin.readline
n, k = map(int,input().split())
res=0
jewels=[]


for _ in range(n):
    tmp =list(map(int,input().split()))
    jewels.append(tmp)


bags=[]
for _ in range(k):
    bags.append(int(input()))

jewels.sort()
bags.sort()


tmp=[]

for bag in bags:
    while jewels and jewels[0][0] <=bag:
        heapq.heappush(tmp,-jewels[0][1])
        heapq.heappop(jewels)
    if tmp:
        res-=heapq.heappop(tmp)


print(res)
        