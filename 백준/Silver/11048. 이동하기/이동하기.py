n,m = map(int,input().split())
lst=[]
for i in range(n):
    tmp = list(map(int,input().split()))
    lst.append(tmp)

dx=[1,0]
dy=[0,1]
ch=[[0 for _ in range(m)] for _ in range(n)]
ch[0][0]=lst[0][0]
for i in range(1,m):
    ch[0][i]=ch[0][i-1]+lst[0][i]

for i in range(1,n):
    ch[i][0]=ch[i-1][0]+lst[i][0]

for i in range(1,n):
    for j in range(1,m):
        ch[i][j]= max(ch[i][j-1]+lst[i][j],ch[i-1][j]+lst[i][j])
    
            
print(ch[n-1][m-1])
    







    