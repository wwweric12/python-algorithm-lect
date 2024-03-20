n= int(input())
lst=list(map(int,input().split()))
lst.insert(0,0)
ch=[0]*(n+1)
for i in range(1,n+1):
    for j in range(i,n+1):
        ch[j] = max(ch[j],ch[j-i]+lst[i])
        
print(ch[-1])
    