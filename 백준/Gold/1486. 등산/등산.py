import sys 
import heapq

input = sys.stdin.readline

dx=[0,1,-1,0] 
dy=[-1,0,0,1]


n,m,t,d = map(int,input().split())

lst=[]
dp= [[1000001 for _ in range(m)] for _ in range(n)]
for i in range(n):
    
    tmp = list(input())
    for j in range(m):
        tmp_num = ord(tmp[j])
        if tmp_num >=97:
            tmp[j] = tmp_num-71
        else:
            tmp[j] = tmp_num-65
    lst.append(tmp)
    


Q=[]
dp[0][0]=0
heapq.heappush(Q,[0,0,0])


while Q:
    time ,x, y =heapq.heappop(Q)
    if dp[y][x] < time:
        continue

    for i in range(4):
        xx = x +dx[i]
        yy = y +dy[i]
        if 0<=xx <m and 0<= yy <n and dp[yy][xx] >time:
            if lst[yy][xx] > lst[y][x]:
                tmp = lst[yy][xx]-lst[y][x]
                nxt_t = tmp*tmp+time
                if tmp > t or nxt_t>d or nxt_t >=dp[yy][xx]:
                    continue
                else:
                    dp[yy][xx] = nxt_t
                    heapq.heappush(Q,[nxt_t, xx,yy])

            else:
                if dp[yy][xx] > time+1:
                    tmp = lst[y][x]-lst[yy][xx]
                    if tmp >t or time+1 >d:
                        continue
                    
                    dp[yy][xx] = time+1
                    heapq.heappush(Q,[time+1,xx,yy])


h_q =[]

heapq.heappush(h_q,(0,0,0))

back = [[1000001 for _ in range(m)] for _ in range(n)]
back[0][0] = 0

while h_q:
    time ,x, y =heapq.heappop(h_q)
    if back[y][x] < time:
        continue    

    for i in range(4):
        xx = x +dx[i]
        yy = y +dy[i]
        if 0<=xx <m and 0<= yy <n and back[yy][xx] >time:
            if lst[yy][xx] < lst[y][x]:
                tmp = lst[y][x]-lst[yy][xx]
                nxt_t = tmp*tmp+time
                if tmp > t or nxt_t>d or nxt_t >=back[yy][xx]:
                    continue
                else:
                    back[yy][xx] = nxt_t
                    heapq.heappush(h_q,[nxt_t,xx,yy])

            else:
                if back[yy][xx] > time+1:
                    tmp = lst[yy][xx]-lst[y][x]
                    if tmp >t or time+1 >d:
                        continue
                    back[yy][xx] = time+1
                    heapq.heappush(h_q,[time+1,xx,yy])

res =0 

for i in range(n):
    for j in range(m):
        if back[i][j]+dp[i][j] <=d :
            res = max(res,lst[i][j])



print(res)


