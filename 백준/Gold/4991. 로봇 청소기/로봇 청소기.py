# (1 ≤ w, h ≤ 20) 
# 로봇 기준으로 가장 가까운 곳을 가야함 ?
# 더러운곳 10개 이하라 경우의 수 360만
# 각각에서 거리 -> 



import heapq 
import sys 

input = sys.stdin.readline

dy = [-1,0,0,1]
dx = [0,1,-1,0]



res = float('inf')


def DFS(L,start,sum_value):
    global len_dirty, res 
    if L == len_dirty-1:
        res = min(res, sum_value)

    if sum_value>= res:
        return 
    
    for i in range(len_dirty):
        if visited[i] == 0:
            visited[i]=1
            DFS(L+1,i,sum_value+distance[start][i])
            visited[i]=0
        


while True:
    w, h = map(int,input().split())
    flag = 0
    res = float('inf')
    if w == 0 and h == 0:
        break
    board=[]
    robot=(0,0)
    dirty=[]
    len_dirty= 0
    for i in range(h):
        tmp = list(input())
        for j in range(w):
            if tmp[j] == "o":
                robot = (i, j)
                tmp[j] = -1 
            elif tmp[j] == "*":
                tmp[j] = len_dirty
                len_dirty+=1
                dirty.append((i,j))
        board.append(tmp)

    distance=[[0 for _ in range(len_dirty+1)] for _ in range(len_dirty+1)] 

    dirty.append(robot)

    for i in range(len_dirty):
        Q= [(0,dirty[i])]
        ch=[[w*h+1 for _ in range(w)] for _ in range(h)]
        ch[dirty[i][0]][dirty[i][1]] = 0
        dp = [0 for _ in range(len_dirty+1)]
        cnt = 1
        while Q:
            if cnt == len_dirty+1:
                break
            power , tmp = heapq.heappop(Q)
            y, x = tmp 

            if ch[y][x] < power and power != 0 :
                continue
            for k in range(4):
                xx = x+dx[k]
                yy = y+dy[k]
                
                if 0<= xx < w and 0<= yy <h and ch[yy][xx] > power+1 and board[yy][xx] !="x":
                    ch[yy][xx] = power+1
                    if board[yy][xx]!=".":
                        dp[board[yy][xx]] = ch[yy][xx]
                        cnt+=1
                    heapq.heappush(Q,(power+1,(yy,xx)))

    
        if cnt != len_dirty+1: 
            flag =1 

            break
        
        for a in range(len_dirty+1):
            distance[i][a] = dp[a]
            distance[a][i] = dp[a]
    if flag == 1:
        print(-1)
    else:
        for i in range(len_dirty):
            visited=[0 for _ in range(len_dirty)]    
            visited[i]= 1
            DFS(0,i,distance[-1][i])
            visited[i]= 0


        
        print(res)

    
                       
        


