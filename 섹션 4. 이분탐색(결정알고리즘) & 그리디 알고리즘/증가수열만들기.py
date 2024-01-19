from collections import deque
n = int(input())

lst=list(map(int,input().split()))

lst=deque(lst)

cnt=0
str=''
tmp =0
while lst:
    if lst[0] <= lst[-1] and tmp <lst[0]:
        tmp =lst.popleft()
        cnt+=1
        str+='L'
    elif lst[0] >= lst[-1] and tmp <lst[-1]:
        tmp =lst.pop()
        cnt+=1
        str+='R'
    elif lst[0]> tmp:
        tmp =lst.popleft()
        cnt+=1
        str+='L'
    elif lst[-1]>tmp:
        tmp =lst.pop()
        cnt+=1
        str+='R'
    else: 
        break

print(cnt)
print(str)
        

#답안


# n = int(input())
# a=list(map(int,input().split()))
# lt =0
# rt = n-1
# last =0
# res =''
# tmp=[]

# while lt<=rt:
#     if a[lt]>last:
#         tmp.append((a[lt],'L'))
#     if a[rt]>last:
#         tmp.append((a[rt],"R"))
#     tmp.sort()
#     if len(tmp) ==0:
#         break
#     else:
#         res=res+tmp[0][1]
#         last = tmp[0][0]
#         if tmp[0][1]=='L':
#             lt+=1
#         else:
#             rt-=1
#     tmp.clear()
# print(len(res))
# print(res)

    
    
    
    


