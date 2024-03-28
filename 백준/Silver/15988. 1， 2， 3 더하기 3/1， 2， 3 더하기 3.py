import sys
input = sys.stdin.readline

n = int(input())


ch=[0]*(1000001)
ch[1]=1
ch[2]=2
ch[3]=4

for i in range(4,1000001):
    ch[i]= (ch[i-1]+ch[i-2]+ch[i-3])%1000000009
    

for i in range(n):
    k = int(input())
    print(ch[k])
    