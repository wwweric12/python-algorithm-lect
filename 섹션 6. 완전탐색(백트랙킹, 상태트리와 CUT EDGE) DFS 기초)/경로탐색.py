def DFS(L,v):
    global cnt
    if v ==n-1 :
        cnt+=1
    elif L == n:
        return
    else:
        for i in range(n):
            if lst[v][i] ==1 and ch[i]==0:
                ch[i]=1
                DFS(L+1,i)
                ch[i]=0
            
                
if __name__ == "__main__":
    n, m = map(int,input().split())
    lst=[n*[0] for _ in range(n)]
    ch=[0]*n
    ch[0]=1
    cnt=0
    for i in range(m):
        a, b = map(int,input().split())
        lst[a-1][b-1]=1
    DFS(0,0)
    print(cnt)
    
#답안 

def DFS(v):
    global cnt
    if v ==n :
        cnt+=1
    else:
        for i in range(1,n+1):
            if g[v][i] ==1 and ch[i]==0:
                ch[i]=1
                DFS(i)
                ch[i]=0
            
                
if __name__ == "__main__":
    n, m = map(int,input().split())
    g=[(n+1)*[0] for _ in range(n+1)]
    ch=[0]*(n+1)
    ch[1]=1
    cnt=0
    for i in range(m):
        a, b = map(int,input().split())
        g[a][b]=1
    DFS(1)
    print(cnt)