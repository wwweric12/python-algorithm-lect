import sys
from collections import deque 

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int,input().split())
    buildings_time =[0]+ list(map(int,input().split()))
    ch=[0 for _ in range(n+1)]
    graph=[[] for _ in range(n+1)]
    for _ in range(k):
        start, end  = map(int,input().split())
        graph[start].append(end)
        ch[end]+=1 
    goal = int(input())
    dp = [0 for _ in range(n+1)]
    Q= deque([])
    for i in range(1,n+1):
        if ch[i] == 0:
            Q.append(i)
            dp[i]= buildings_time[i]
            
    
    
    while Q:
        node = Q.popleft()
        if node == goal:
            print(dp[node])
            break
        for i in graph[node]:
            ch[i]-=1
            dp[i]= max(dp[i],dp[node]+buildings_time[i])
            if ch[i]== 0:
                Q.append(i)
        
        
    
          
    