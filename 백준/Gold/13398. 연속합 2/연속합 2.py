import sys

input = sys.stdin.readline

n = int(input())


ch1=[0]*n
ch2=[0]*n
lst=list(map(int,input().split()))
ch1[0]=lst[0]
ch2[0]=lst[0]
for i in range(1,n):
    ch1[i]=max(ch1[i-1]+lst[i],lst[i])
    ch2[i]=max(ch1[i-1],ch2[i-1]+lst[i])


print(max(max(ch1),max(ch2)))