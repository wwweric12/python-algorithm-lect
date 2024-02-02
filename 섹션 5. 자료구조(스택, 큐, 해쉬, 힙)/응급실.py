from collections import deque

n, m = map(int,input().split())
lst=list(map(int,input().split()))

tmp=[]
for i in range(n):
    tmp.append((lst[i],i))

dque=deque(tmp)

cnt=0
while True: 
    k = dque.popleft()
    if k[0] < max(dque)[0]:
        dque.append(k)
    else:
        cnt+=1
        if k[1] == m :
            break
    
print(cnt)

#답안 

# n, m = map(int,input().split())
# Q=[(pos,val) for pos,val in enumerate(list(map(int,input().split())))]

# Q= deque(Q)
# cnt =0 

# while True:
#     cur = Q.popleft()
#     if any(cur[1]<x[1] for x in Q): # any는 단한번이라도 참이면 참이다 
#         Q.append(cur)
#     else:
#         cnt+=1
#         if cur[0] == m :
#             break

# print(cnt)

    

    