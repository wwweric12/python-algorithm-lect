n ,t = map(int,input().split())


lst=[i+1 for i in range(n)]

res=[]
k = t-1
while lst:
    if len(lst)==1:
        res.append(lst.pop())
        break
    res.append(lst.pop(k))
    k+=t-1
    if k >= len(lst):
        k%=len(lst)
        
print("<",end='')
for i in range(len(res)):
    if i == len(res)-1:
        print(res[i],end="")
    else:
        print(res[i],end="")
        print(",",end=" ")
    

print(">")