import math

n = int(input())

k=int(math.sqrt(n))+1

ch=[n]*(n+1)
ch[0]=0
ch[1]=1
for i in range(1,k+1):
    for j in range(i*i,n+1):
        ch[j]=min(ch[j],ch[j-i*i]+1)
    
print(ch[n])

