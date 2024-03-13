import sys
input = sys.stdin.readline

def gcd(a,b):
    while b> 0:
        a, b = b, a%b
    return a
    
n=int(input())

for i in range(n):
    lst=list(map(int,input().split()))
    res=0
    for j in range(1,lst[0]):
        for k in range(j+1,lst[0]+1):
            res+=gcd(lst[j],lst[k])
    print(res)