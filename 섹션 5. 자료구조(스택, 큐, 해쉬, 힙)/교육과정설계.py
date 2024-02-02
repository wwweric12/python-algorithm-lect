k=input()
n=int(input())

for x in range(n):
    c=input()
    lst=["0"]
    for t in c:
        if t in k and lst[-1] !=t:
            lst.append(t)
    tmp="".join(lst)
    if k in tmp:
        print("#"+str(x+1)+' ' +"YES")
    else:
        print("#"+str(x+1)+' ' +"NO")

#답안

# from collections import deque

# need = input()
# n= int(input())

# for i in range(n):
#     plan = input()
#     dq=deque(need)
#     for x in plan:
#         if x in dq:
#             if x !=dq.popleft(): #맨앞자료와 일치하지않으면 순서 어긋난거
#                 print("#%d NO" %(i+1))
#                 break
#     else: 
#         if len(dq)==0:
#             print("#%d YES" %(i+1))
#         else:
#             print("#%d NO" %(i+1))
            
            
    
    
    
