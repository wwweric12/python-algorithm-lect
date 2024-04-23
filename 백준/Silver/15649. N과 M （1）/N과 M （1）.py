import sys

input = sys.stdin.readline

n,m =map(int,input().split())

ch=[0]*(n+1)
res=[0]*(m+1)
def DFS(L):
    if L == m:
        for j in range(1,m+1):
            print(res[j],end=' ')
        print()
        
    else:
        for i in range(1,n+1):
            if ch[i]==0:
                ch[i]=1
                res[L+1]=i
                DFS(L+1)
                ch[i]=0
        
    
DFS(0)