import sys
from collections import deque 

n, m = map(int,input().split())

ch=[[]for _ in range(n+1)]
in_queue = [0 for _ in range(n+1)]
dp=[10**9 for _ in range(n+1)]
count=[0 for _ in range(n+1)]

Q =deque()

for i in range(m):
    start, end ,d = map(int,input().split())    
    ch[start].append([end,d])



Q.append(1)
dp[1]=0
in_queue[1]=1

while Q:
    index = Q.popleft()
    in_queue[index] = 0
    for end ,d in ch[index]:
        if dp[end] > dp[index]+d:
            dp[end] = dp[index]+d
            if in_queue[end] == 0:
                Q.append(end)
                in_queue[end]=1
                count[end]+=1
                if count[end]>=n:
                    print(-1)
                    sys.exit()
        
    
for i in range(2,n+1):
    if dp[i]==10**9:
        print(-1)
    else:
        print(dp[i])
    
    


        