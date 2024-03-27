import sys
input=sys.stdin.readline

n= int(input())
lst=list(map(int,input().split()))
ch=[0]*(n+1)

ch[0]=lst[0]
max_value = lst[0]
for i in range(1,n):
    ch[i] = max(lst[i],ch[i-1]+lst[i])
    if max_value < ch[i]:
        max_value =ch[i]

print(max_value)
        
        

