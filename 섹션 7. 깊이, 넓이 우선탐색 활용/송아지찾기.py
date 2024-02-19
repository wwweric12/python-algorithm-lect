s,e =map(int,input().split())
k = (e-s)//5
t=(e-s)%5
if k <0:
    res = s-e
else:
    if t ==4:
        res=k+2
    else:
        res=k+ t
print(res)

#답안 
#BFS 레벨탐색 큐 구조  // 0번이 pop되서 나오면 0이랑 이어져있는 모든 노드(레벨)들이 큐에 들어감(탐색) 이런식을 진행 

from collections import deque
MAX = 10000

ch = [0] * (MAX+1)
dis = [0] * (MAX+1)
n,m = map(int,input().split())
ch[n] = 1 # 체크
dis[n] = 0 # 얼마만에 왔는지
dq = deque()
dq.append(n)
while dq:
    now = dq.popleft()
    if now == m:
        break
    for next in(now-1,now+1,now+5): # 3가지로 for문이 돈다
        if 0< next <=MAX:
            if ch[next] ==0:
                dq.append(next)
                ch[next]=1
                dis[next]=dis[now]+1
                
print(dis[m])