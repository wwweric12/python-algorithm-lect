import heapq
import sys
##  (1 ≤ V ≤ 20,000, 1 ≤ E ≤ 300,000)

## 가중치가 음수는 없음
## 정점 사이에는 여러개의 간선이 존재할 수 있음
## 다익스트라를 모든 부분에 대해서 해주는 방법으로 가즈아 
input= sys.stdin.readline
v, e = map(int,input().split())
start = int(input())

e_lst=[[] for _ in range(v)]

for _ in range(e):
    a, b, w = map(int,input().split())
    e_lst[a-1].append((b-1,w))
    

ch=[0 for _ in range(v)] ## 방문 체크 
distance=[200001 for _ in range(v)] ## 최종 결과 
distance[start-1]=0


heap =[]
heapq.heappush(heap,(0,start-1))



# 1. 첫번째 시작지점 넣고
# 2. 시작지점과 연결된 간선에 대해서 갱신 하고 방문하지 않은 곳이면 우선순위 큐에 넣기

while heap:
    priority, node = heapq.heappop(heap)
    if distance[node] < priority:
        continue
    
    ch[node]=1
    for end, w in e_lst[node]:
        if distance[end] > distance[node]+w:
            distance[end]=distance[node]+w
            heapq.heappush(heap,(distance[end],end))
    
            
        
for i in distance:  
    if i == 200001:
        print("INF")
    else:
        print(i)
        
    
            
        
        
    