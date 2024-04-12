import sys
input= sys.stdin.readline

n = int(input())
m = int(input())


if m== 0:
    lst=[]
else:
    lst=list(map(int,input().split()))
res = abs(n-100)
for i in range(1000000):
    for j in str(i):
        if  int(j) in lst:
            break
    else:
        res =min(res,abs(n-i)+len(str(i)))
print(res)