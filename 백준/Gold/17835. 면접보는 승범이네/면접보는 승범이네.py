# n 개의 도시 중 k개의 도시에 면접장 배치 
import heapq

import sys 
input = sys.stdin.readline


n, m, k = map(int,input().split())

lst =[[] for _ in range(n+1)]

for i in range(m):
    u,v, c = map(int,input().split())
    lst[v].append((u,c))



interview = list(map(int,input().split()))

dp=[float('inf') for _ in range(n+1)]


Q=[]

for i in interview:
    
    heapq.heappush(Q,(0,i))



while Q:
    value, node = heapq.heappop(Q)

    if dp[node] <value:
        continue
    
    dp[node] = value

    for nxt, w in lst[node]:
        if dp[nxt] > value+w:
            dp[nxt] = value+w
            heapq.heappush(Q,(value+w,nxt))
    
max_value = 0
max_index = 0
for i in range(1,n+1):
    if max_value < dp[i]:
        max_index = i
        max_value = dp[i]

print(max_index)
print(max_value)

