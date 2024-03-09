import sys
input = sys.stdin.readline

n= int(input())
lst =list(map(int,input().split()))
mv=max(lst)
ch=[0]*(mv+1)
res = [-1]*n
stack=[]

for i in lst:
    ch[i]+=1
    

for i in range(n):
    tmp = ch[lst[i]]
    while stack and tmp > stack[-1][1]:
        res[stack.pop()[0]]=lst[i]
    stack.append((i,tmp))
        
    
for i in res:
    print(i,end=' ')