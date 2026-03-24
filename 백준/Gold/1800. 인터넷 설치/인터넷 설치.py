import sys

import heapq

input = sys.stdin.readline

n, p, k = map(int,input().split())


lst=[[]for _ in range(n+1)]

for _ in range(p):
    a,b, w = map(int,input().split())
    lst[a].append((b,w))
    lst[b].append((a,w))


Q = []

dp=[[float('inf') for _ in range(k+1)] for _ in range(n+1)]


dp[n][0] =0


heapq.heappush(Q,(0,0,n))


while Q:
    value, cnt, node = heapq.heappop(Q)
        ## 값이 작아야 의미가 있ㅇ니까    
    if dp[node][cnt] < value :
        continue
    
    for nxt,w in lst[node]:
        tmp = max(value,w) 
        if dp[nxt][cnt] > tmp:
            dp[nxt][cnt] =tmp
            heapq.heappush(Q,(tmp,cnt, nxt))
        
        if cnt < k:
            if dp[nxt][cnt+1] > value:
                dp[nxt][cnt+1] = value
                heapq.heappush(Q,(value,cnt+1, nxt))
            

ans = min(dp[1])
if ans== float('inf'):
    print(-1)
else:
    print(ans)
