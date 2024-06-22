import sys
n = int(input())
lst=list(map(int,input().split()))


for i in range(n-1,0,-1):
    if lst[i] <lst[i-1]:
        for j in range(n-1,0,-1):
            if lst[j] <lst[i-1]:
                lst[j],lst[i-1] = lst[i-1], lst[j]
                lst =lst[:i]+sorted(lst[i:],reverse=True)
                for k in lst:
                    print(k,end=' ')
                sys.exit()
                
else:
    print(-1)

