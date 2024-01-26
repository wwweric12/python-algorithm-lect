n,m=map(int,input().split())

lst=[]
for i in str(n):
    lst.append(int(i))
    
cnt=0

while m!=0:
    if lst[-m:] == lst[cnt:m+cnt]:
        for _ in range(m):
            lst.pop(-1)
        break
    tmp = max(lst[cnt:m+cnt+1])
    k=lst[cnt:m+cnt+1].index(tmp)
    for _ in range(k):
        lst.pop(cnt)
        m-=1
    cnt+=1

tmp=''
for i in lst:
    tmp+=str(i)
print(int(tmp))
    
    
#답안 (스택구조)

# num,m=map(int,input().split())
# num =list(map(int,str(num)))

# stack=[]
# for x in num:
#     while stack and m>0 and stack[-1]<x :
#         stack.pop()
#         m-=1
#     stack.append(x)
# if m!=0:
#     stack=stack[:-m]

# res = ''.join(map(str,stack))
# print(res)

