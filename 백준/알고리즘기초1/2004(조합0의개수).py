import sys
input=sys.stdin.readline

n , m = map(int,input().split())

def div_count(k,s):
    res =0
    while k!=0:
        k//=s
        res+=k
    return res

print(min(div_count(n,2)-div_count(m,2)-div_count(n-m,2),div_count(n,5)-div_count(m,5)-div_count(n-m,5)))



