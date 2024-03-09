import sys

input = sys.stdin.readline

n = int(input())
lst=list(map(int,input().split()))
res=[-1]*n
stack=[]
for i in range(n):
    while stack and lst[stack[-1]]<lst[i]:
        res[stack.pop()]  = lst[i]
    stack.append(i)

for i in res:
    print(i,end=' ')