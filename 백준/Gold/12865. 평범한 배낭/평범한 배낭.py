import sys
input = sys.stdin.readline

n, k = map(int,input().split())

ch=[0 for _ in range(k+1)]

for _ in range(n):
    w, v = map(int,input().split())
    for i in range(k,w-1,-1):
        ch[i]=max(ch[i],ch[i-w]+v)

print(ch[-1])
    

