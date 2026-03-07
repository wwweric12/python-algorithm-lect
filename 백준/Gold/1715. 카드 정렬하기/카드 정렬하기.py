# 이전꺼의 합이 다음꺼로 가기 때문에 최소한의 합으로 더해 나가는게 좋은데 
# 10만 이니까 sort를 하면 10만 log 10만?
import sys 
import heapq

input = sys.stdin.readline

n = int(input())

hq=[]

for i in range(n):
    heapq.heappush(hq,int(input()))
    


if n == 1 :
    print(0)
    sys.exit()
    
res= 0
cnt=0
while hq:
    if cnt == n-1:
        break
    node1 = heapq.heappop(hq)
    node2 = heapq.heappop(hq)
    value= node1+node2
    res+=value
    heapq.heappush(hq,value)
    cnt+=1
    
    
    
print(res)








