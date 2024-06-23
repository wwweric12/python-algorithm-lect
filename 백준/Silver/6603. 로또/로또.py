lst=[]
ch=[]
while True:
    tmp=list(map(int,input().split()))
    if len(tmp)==1:
        break
    else:
        ch.append([0]*(tmp[0]+1))
        lst.append(tmp)
        
res=[]




def DFS(L,F,S):
    if L==6:
        for i in res:
            print(i,end=' ')   
        print()
        return
    else:
        for i in range(S,len(lst[F])):
            if ch[F][i]==0:
                ch[F][i]=1
                res.append(lst[F][i])
                DFS(L+1,F,i)
                res.pop()
                ch[F][i]=0
                
        
    
        
for i in range(len(lst)):
    DFS(0,i,1)
    print()

    