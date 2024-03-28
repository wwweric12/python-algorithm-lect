import sys
input = sys.stdin.readline
n=int(input())

res=0
ch=[[0,0,0] for _ in range(n+1)]

for i in range(1,n+1):
    lst=list(map(int,input().split()))
    ch[i][0]=min(lst[0]+ch[i-1][1],lst[0]+ch[i-1][2])
    ch[i][1]=min(lst[1]+ch[i-1][0],lst[1]+ch[i-1][2])
    ch[i][2]=min(lst[2]+ch[i-1][1],lst[2]+ch[i-1][0])
 
print(min(ch[n])) 