import sys
input = sys.stdin.readline

n = int(input())
graph=[]
for _ in range(n):
    tmp = list(map(int,input().split()))
    graph.append(tmp)



## 어디서 시작하는 것은 상관없음
## 1->2->3->4->1 이런식인데



dp=[[16000001 for _ in range(2**n)] for _ in range(n)]


def DFS(now,path):    
    if path == (1<< n) -1:
        if graph[now][0]:
            return graph[now][0]
        else:
            return 16000002
    if dp[now][path] != 16000001:
        return dp[now][path]
    
    
    dp[now][path] = 16000002
    
    for i in range(1,n):
        if not graph[now][i]:
            continue
        if path & (1<<i): 
            continue 
        dp[now][path] = min(dp[now][path],DFS(i,path | (1<<i)) + graph[now][i])
    return dp[now][path]
    


print(DFS(0,1))
                


