import heapq as hq
import sys
input = sys.stdin.readline


a=[]
while True:
    n=int(input())
    if n == 0:
        if a:
            print(hq.heappop(a))
        else:
            print(-1)
    elif n== -1:
        break
    else:
        hq.heappush(a,n)        
        hq._heapify_max(a)
        
    
# #답안
# #최소힙에서 부호를 반대로 바꿔서 최대힙으로 만든다


a=[]
while True:
    n=int(input())
    if n == 0:
        if a:
            print(-hq.heappop(a))
        else:
            print(-1)
    elif n== -1:
        break
    else:
        hq.heappush(a,-n)        




    
    

