import sys
import heapq
input = sys.stdin.readline


n = int(input())

lst=[[] for _ in range(n+1)]

Q=[]
for i in range(n):
    d, w = map(int,input().split())
    heapq.heappush(lst[d],-w)
    


dp=[0 for _ in range(n+1)]


for i in range(n,0,-1):
    for j in lst[i]:
        heapq.heappush(Q,j)
    if Q:
        w = heapq.heappop(Q)
        dp[i] = -w


print(sum(dp[1:]))

