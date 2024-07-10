n = int(input())
lst=list(map(int,input().split()))
ch=[10000]*n
ch[0]=1
for i in range(n):
    for j in range(1,lst[i]+1):
        if i+j <n:
            if i==0:
                ch[i+j]=1
                
            else:
                ch[i+j]=min(ch[i+j],ch[i]+1)
ch[0]=0
if ch[-1]==10000:
    print(-1)
else:
    print(ch[-1])