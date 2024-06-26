n ,s = map(int,input().split())
lst = list(map(int,input().split()))

ch = [0]*n
res=0
tmp=0
def DFS(L):
    global tmp,res
    if L == n:
        if  1 in ch:
            for i in range(n):
                if ch[i]==1:
                    tmp+=lst[i]
            if tmp ==s:
                res+=1
            tmp=0
        return
    else:
        ch[L]=1
        DFS(L+1)
        ch[L]=0
        DFS(L+1)
        
                

DFS(0)
print(res)