n= int(input())
lst=[]
for i in range(n):
    lst.append(list(map(int,input().split())))

ch=[0]*n
min=100000000

def DFS(L,next,S,f):
    global min
    if L == n-1:
        if min >S+lst[next][f] and lst[next][f]!=0:
            min=S+lst[next][f]
        return
    else:
        for i in range(n):
            if lst[next][i]!=0 and ch[i]==0:
                ch[i]=1
                DFS(L+1,i,S+lst[next][i],f)
                ch[i]=0


for t in range(n):
    ch[t]=1
    DFS(0,t,0,t)
    ch[t]=0


print(min)