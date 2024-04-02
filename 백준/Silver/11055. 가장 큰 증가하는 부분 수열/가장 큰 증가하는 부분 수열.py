import sys
input=sys.stdin.readline

n= int(input())
lst=list(map(int,input().split()))

ch=[0 for _ in range(n)]
ch[0]=lst[0]

for i in range(1,n):
    for j in range(i):
        if lst[i] > lst[j] and ch[i] < ch[j] +lst[i]:
            ch[i]= lst[i]+ch[j]
    
    if ch[i]==0:
        ch[i]=lst[i]
        
print(max(ch))