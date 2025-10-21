import heapq
n, k = map(int,input().split())
lst = list(map(int,input().split()))



## n이 30만이라 완전탐색은 안되고 
## dp나 그리디로 풀어야 할거 같은데 

hq=[] 

ch =[0 for _ in range(n-1)]
for i in range(n-1):
    ch[i] = lst[i+1]-lst[i]
    heapq.heappush(hq,-ch[i])
    

res= sum(ch)

for j in range(k-1):
    value =heapq.heappop(hq)
    res+=value

print(res)
    
    




  