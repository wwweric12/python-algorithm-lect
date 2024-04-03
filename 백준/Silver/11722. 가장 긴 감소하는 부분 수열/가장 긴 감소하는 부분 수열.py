import sys
input = sys.stdin.readline

n= int(input())

lst=list(map(int,input().split()))
ch=[0]*n

ch[0]=1


for i in range(n):
    for j in range(i,-1,-1):
        if lst[i]< lst[j] and ch[i] <= ch[j]:
            ch[i]=ch[j]+1
    if ch[i]==0:
        ch[i]=1
    

print(max(ch))