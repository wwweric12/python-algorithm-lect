n= int(input())
lst=list(map(int,input().split()))

dy=[0]*n
dy[0]=1

for i in range(1,n):
    tmp=0
    for j in range(i-1,-1,-1):
        if lst[i]> lst[j] and tmp < dy[j]:
            tmp = dy[j]
    dy[i]=tmp+1
    

print(max(dy))




