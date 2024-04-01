import sys
input = sys.stdin.readline

n=int(input())
lst=[]
ch0=[0 for _ in range(n)]
ch1=[0 for _ in range(n)]
for _ in range(n):
    lst.append(int(input()))

ch0[0]=lst[0]
ch1[0]=lst[0]
if n>1:
    ch1[1]=lst[0]+lst[1]
    ch0[1]=lst[1]
    for i in range(2,n):
        ch0[i]=max(lst[i]+max(ch1[i-2],ch0[i-2]),ch1[i-1])
        ch1[i]=lst[i]+ch0[i-1]
        

print(max(ch0[n-1],ch1[n-1]))

