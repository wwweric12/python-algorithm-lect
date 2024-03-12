import sys
input= sys.stdin.readline


a ,b = map(int,input().split())

def gcd(a,b):
    while b>0:
        a,b = b, a%b
    return a

print(gcd(a,b)) # a와 b의 최대공약수는 b 와 a%b의 최대공약수와 같다 
print(a*b//gcd(a,b)) # a= x*gcd(a,b)  b= y*gcd(a,b) 이기 떄문에 a*b/gcd(a*b)