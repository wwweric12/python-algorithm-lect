n = int(input())

lst=[[] for _ in range(10001)]


for i in range(n):
    p,d = map(int,input().split())
    lst[d].append(p)
res=0
    
for i in range(n,0,-1):
    tmp =0
    tmp_idx=0
    for j in range(i,10001):
        if  lst[j]!=[] and max(lst[j])>tmp:
            tmp_idx=j
            tmp=max(lst[j])
    if tmp !=0:
        res+=tmp
        lst[tmp_idx].remove(tmp)

print(res)
        

     


