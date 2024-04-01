import sys
input = sys.stdin.readline

n= int(input())
lst=[]
ch=[]
for _ in range(n):
    tmp=list(map(int,input().split()))
    lst.append(tmp)
    ch.append(tmp)

for i in range(1,n):
    ch[i][i]=ch[i-1][i-1]+lst[i][i]
    ch[i][0]=ch[i-1][0]+lst[i][0]
    for j in range(1,i):
        ch[i][j]=lst[i][j]+max(ch[i-1][j-1],ch[i-1][j])
     


print(max(ch[n-1]))
