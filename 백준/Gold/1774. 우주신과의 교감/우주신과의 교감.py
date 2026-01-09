## 연결되지 않은 좌표에서 가장 가까운 좌표(연결된)를 찾아서 
## 해당 거리를 더해주면된다. 
## 그러면 가장 가까운 좌표를 어떻게 찾으면좋을까?
## 하지만 이게 지금은 연결 안된거 지만 나중에 연결되는것을 찾아야하는데

## 1. 연결된 좌표에서 우선 연결되지 않은 좌표를 탐색 
## 2. 그 좌표들에서 가장짧은 좌표를 더하는 방식이 맞는거 같은데? 

import math 



n, m = map(int,input().split())


god=[0]
for _ in range(n): 
    god.append(list(map(int,input().split())))


dist=[[float('inf') for _ in range(1001)] for _ in range(1001)]

for i in range(1,n+1):
    for j in range(i,n+1):
        tmp= math.sqrt((god[i][0]-god[j][0])**2+ (god[i][1]-god[j][1])**2)
        dist[i][j] =tmp
        dist[j][i] = tmp

for _ in range(m):
    a,b = map(int,input().split())
    dist[a][b]=0
    dist[b][a]=0



dist_value = [float('inf') for _ in range(n+1)]
ch = [0 for _ in range(n+1)]
dist_value[1] = 0 
res = 0


for _ in range(n):
    min_index =-1
    min_value = float('inf')
    for i in range(1,n+1):
        if ch[i] == 0 and min_value> dist_value[i]:
            min_index = i 
            min_value = dist_value[i]

    if min_index == -1:
        break

    ch[min_index] = 1

    res+=min_value

    for i in range(1, n+1):
        if ch[i] == 0 :
            if dist[min_index][i] < dist_value[i]:
                dist_value[i] = dist[min_index][i]




print(format(res,".2f")) 
   


