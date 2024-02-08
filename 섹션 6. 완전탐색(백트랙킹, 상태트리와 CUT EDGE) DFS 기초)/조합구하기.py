def DFS(v):
    global cnt
    if v == m:
        for i in range(v):
            print(res[i],end=' ')
        print()
        cnt+=1
        return
    else:
        for i in range(1,n+1):
            if ch[i] == 0 :
                for j in range(i+1):
                    ch[j]=1    
                res[v]=i
                DFS(v+1)
                for j in range(i+1):
                    ch[j]=0  
                
                
if __name__ == "__main__":
    n, m = map(int,input().split())    
    ch=[0]*(n+1)
    res=[0]*n
    cnt =0
    DFS(0)
    print(cnt)
    
#답안

def DFS(L,s):
    global cnt
    if L == m:
        for j in range(L):
            print(res[j], end =' ')
        cnt+=1
        print()
    else:
        for i in range(s, n+1):
            res[L]= i
            DFS(L+1,i+1)




if __name__ == "__main__":
    n, m = map(int,input().split())    
    res=[0]*(n+1)
    cnt =0
    DFS(0,1)
    print(cnt)