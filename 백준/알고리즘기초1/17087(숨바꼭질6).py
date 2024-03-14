import sys
input = sys.stdin.readline
n, s =map(int,input().split())
lst=list(map(int,input().split()))

def gcd(a,b):
    while b>0:
        a, b = b ,a%b
    return a

min_v = 1000000000
for i in range(n):
    lst[i]=abs(lst[i]-s)
lst.sort()

if len(lst)==1:
    min_v=lst[0]
    
else:
    for i in range(1,len(lst)):
        tmp = gcd(lst[0],lst[i])
        if tmp < min_v:
            min_v= tmp

print(min_v)
       

            
