n , k = map(int,input().split())
lst=[]
for _ in range(n):
    lst.append(int(input()))
    
cnt=0
while k!=0:
    for i in range(n-1,-1,-1):
        if lst[i]<=k:
            cnt+=k//lst[i]
            k%=lst[i]

    
print(cnt)