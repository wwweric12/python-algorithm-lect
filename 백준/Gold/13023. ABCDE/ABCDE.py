import sys
input = sys.stdin.readline

n, m = map(int,input().split())

ch= [[] for _ in range(n)]
ck=[0]*n

for i in range(m):
    tmp=list(map(int,input().split()))
    ch[tmp[0]].append(tmp[1])
    ch[tmp[1]].append(tmp[0])


def DFS(L,S):
    if L == 4:
        print(1)
        sys.exit()
        
    else:
        for i in ch[S]:
            if ck[i]==0:
                ck[i]=1
                DFS(L+1,i)
                ck[i]=0
                
                
    
for i in range(n):
    ck[i]=1
    DFS(0,i)
    ck[i]=0
    
else:
    print(0)



    
        
    
