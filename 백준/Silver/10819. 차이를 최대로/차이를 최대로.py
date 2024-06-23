n= int(input())
lst = list(map(int,input().split()))

ch=[0]*n

res=[]

max_value=0
def DFS(L):
    global max_value
    if L ==n:
        tmp=0
        for j in range(1,n):
            tmp+=abs(res[j]-res[j-1])    
        if max_value < tmp:
            max_value=tmp
        return 
        
    else:
        for i in range(n):
            if ch[i]==0:
                ch[i]=1
                res.append(lst[i])
                DFS(L+1)
                res.pop()
                ch[i]=0


DFS(0)

print(max_value)

    