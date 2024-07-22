import sys
from collections import deque 
sys.setrecursionlimit(10**6)
Q=deque()

n, k = map(int,input().split())

distance=[0]*100001


Q.append(n)     
while Q:
    tmp=Q.popleft()
    if tmp ==k:
        print(distance[tmp])
        
        break
    for i in (tmp-1,tmp+1,tmp*2):
        if 0<= i <=100000  and distance[i] ==0:
            distance[i]=distance[tmp]+1
            Q.append(i)
    



    
    
    
    
    
    


