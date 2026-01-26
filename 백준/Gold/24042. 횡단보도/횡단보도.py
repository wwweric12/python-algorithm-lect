import heapq
import sys

input = sys.stdin.readline
n, m = map(int,input().split())

## n은 10만 까지
## m은 70만 까지 


## 0으로 채운 이중배열은 안되는데 
## DP에 저장해서 해야할거같은데

## 완탐으로 구현하면 70만번을 10만번 할 수 있어서 안됨
## 그러면 그리디 같이 해야할거같은데
## 각각의 연결된 부분이 주기의 몇번째인지 계속 저장해놓고 시작? 해야할거같은데 





lst =[[] for _ in range(n+1)]


for i in range(m):
    s, e = map(int,input().split())
    lst[s].append((e,i+1))
    lst[e].append((s,i+1))    


dp=[float("inf") for _ in range(n+1)]
dp[1]= 0

Q=[]
heapq.heappush(Q,(0,1))

while Q:
    time,node = heapq.heappop(Q)
    
    for tmp in lst[node]:
        nxt, nxt_time = tmp
        tmp_time = time%m
    
        if nxt_time > tmp_time:
            result=time+nxt_time-tmp_time
        elif nxt_time < tmp_time:
            k = time//m
            result= nxt_time+(k+1)*m
        
        if dp[nxt] > result:
            dp[nxt] = result
            heapq.heappush(Q,(result,nxt))
    


print(dp[-1])