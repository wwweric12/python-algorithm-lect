def DFS(v,sum,l):
    global res
    if v >m:
        if sum-l >res :
            res= sum-l
        return
    else:
        for i in range(n):
            if ch[i]==0:
                ch[i]=1
                DFS(v+lst[i][1],sum+lst[i][0],lst[i][0])
                ch[i]=0
        
        
if __name__ == "__main__":
    n, m = map(int,input().split())
    lst=[]
    res=0
    total=0
    ch=[0]*n
    for _ in range(n):
        lst.append(list(map(int,input().split())))
    DFS(0,0,0)
    print(res)


#답안
def DFS(L,sum,time):
    global res 
    if time >m :
        return
    if L == n :
        if sum > res:
            res =sum
    else:
        DFS(L+1,sum+pv[L],time+pt[L])
        DFS(L+1,sum,time)
        
if __name__ == "__main__":
    n, m = map(int,input().split())
    pv=list()
    pt=list()
    
    for _ in range(n):
        a,b=(map(int,input().split()))
        pv.append(a)
        pt.append(b)
    res=-2147000000
    DFS(0,0,0)
    print(res)


        