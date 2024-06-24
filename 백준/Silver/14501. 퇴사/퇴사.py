n=int(input())
lst=[]
for i in range(n):
    tmp=list(map(int,input().split()))
    lst.append(tmp)

ch=[0]*(n+1)

for j in range(n):
    for k in range(lst[j][0]+j,n+1):
        if ch[k] < ch[j]+lst[j][1]:
            ch[k]= ch[j]+lst[j][1]
    
            

print(ch[-1])
    

