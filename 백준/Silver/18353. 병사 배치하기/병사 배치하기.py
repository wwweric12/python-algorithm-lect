import sys
n = int(input())
lst= list(map(int,input().split()))

ch=[1 for _ in range(n)]


for i in range(1,n):
    for j in range(i):
        if lst[j] > lst[i]:
            ch[i]=max(ch[i],ch[j]+1)

print(n-max(ch))


        
