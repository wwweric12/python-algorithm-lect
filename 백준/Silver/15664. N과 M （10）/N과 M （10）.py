import sys
input = sys.stdin.readline

n, m = map(int,input().split())
lst = list(map(int,input().split()))

max_value=max(lst)+1
ch=[0]*max_value

for i in lst:
    ch[i]+=1

res=[]



def DFS(L,p):
    if L==m:
        for i in res:
            print(i,end=' ')
        print()
        return
    else:
        for i in range(p,max_value):
            if ch[i]!=0:
                ch[i]-=1
                res.append(i)
                DFS(L+1,i)
                res.pop()
                ch[i]+=1
                

DFS(0,0)
    
    

