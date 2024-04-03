import sys
input = sys.stdin.readline


n= int(input())

lst =list(map(int,input().split()))

ch_up=[1]*n
ch_down=[1]*n


res=0
for i in range(n):
    for j in range(i,-1,-1):
        if lst[j]<lst[i] and ch_up[i]<=ch_up[j]:
            ch_up[i]=ch_up[j]+1
    for j in range(n-i-1,n):
        if lst[n-i-1]> lst[j] and ch_down[n-i-1]<=ch_down[j]:
            ch_down[n-i-1]=ch_down[j]+1
    
    
for i in range(n):
    res= max(res,ch_down[i]+ch_up[i])



print(res-1)

    
        
                