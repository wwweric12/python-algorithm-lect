import heapq 

def solution(m, n, puddles):
    answer = 0
    dx= [-1,0,0,1] 
    dy= [0,1,-1,0]
    Q =[]
    dp = [[[float('inf'),0] for _ in range(m)] for _ in range(n)]
    dp[0][0] = [0,1]
    heapq.heappush(Q,(1,0,0))
    
    for puddle in puddles:
        dp[puddle[1]-1][puddle[0]-1] = [-1,0]
    
    while Q:
        value, y, x = heapq.heappop(Q)
        
        if value != dp[y][x][0] + 1:
            continue
        
        for i in range(4):
            yy = y + dy[i]
            xx = x + dx[i]
            if 0<= yy < n and 0<= xx < m:
                if dp[yy][xx][0] == value:
                    dp[yy][xx][1]=(dp[yy][xx][1] + dp[y][x][1])%1000000007
                elif dp[yy][xx][0] > value:
                    dp[yy][xx][0] = value 
                    dp[yy][xx][1] = dp[y][x][1]%1000000007
                    heapq.heappush(Q,(value+1,yy,xx))


    
    answer = dp[n-1][m-1][1]
    
    return answer