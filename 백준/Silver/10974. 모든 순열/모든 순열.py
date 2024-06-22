n= int(input())

ch=[0]*(n+1)
res=[]

def DFS(L):
    if L==n:
        for i in res:
            print(i,end=' ')
        print()
    else:
        for i in range(1,n+1):
            if ch[i]==0:
                ch[i]=1
                res.append(i)
                DFS(L+1)
                res.pop()
                ch[i]=0
                

DFS(0)