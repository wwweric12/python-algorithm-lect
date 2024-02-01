n, k = map(int,input().split())

queue=[]
for i in range(1,n+1):
    queue.append(i)

while len(queue)!=1:
    for _ in range(k-1):
        tmp=queue.pop(0)
        queue.append(tmp)
    queue.pop(0)
                
print(queue[0])
    
#답안 

# from collections import deque
# n, k = map(int,input().split())

# dq= list(range(1,n+1))
# dq =deque(dq)

# while dq:
#     for _ in range(k-1):
#         cur=dq.popleft()
#         dq.append(cur)
#     dq.popleft()
#     if len(dq) ==1:
#         print(dq[0])
#         dq.popleft()
    