import heapq
import sys

input= sys.stdin.readline
n, m = map(int,input().split())

lst= []

start=(0,0)
res=(0,0)

visited=[[(float('inf'),float('inf')) for _ in range(m)] for _ in range(n)]

Q=[]

for i in range(n):
    tmp=list(input())
    for j in range(m):
        if tmp[j]=="S":
            start= (i,j)
            
    lst.append(tmp)



heapq.heappush(Q,(0,0, start[0], start[1]))

dy=[-1,0,0,1]
dx=[0,1,-1,0]


while Q:
    across,side, y,x  = heapq.heappop(Q)
    
    if lst[y][x] == "F":
        res = (across,side)
        break 
    
    if visited[y][x][0] < across:
        continue
    if visited[y][x][0] == across:
        if visited[y][x][1] < side:
            continue
    
    
    for i in range(4):
        yy = y+dy[i]
        xx = x+dx[i]
        if 0 <= yy< n and 0<= xx <m:
            tmp_across=across 
            tmp_side=side 
            if lst[yy][xx]=="g":
                tmp_across+=1        
    
            elif lst[yy][xx] ==".":
                for j in range(4):
                    yyy = yy+dy[j]
                    xxx = xx+dx[j]
                    if 0 <= yyy< n and 0<= xxx <m:
                        if lst[yyy][xxx] =="g":
                            tmp_side+=1
                            break
            if visited[yy][xx][0] < tmp_across:
                continue
            if visited[yy][xx][0] == tmp_across:
                if visited[yy][xx][1] <= tmp_side:
                    continue
            visited[yy][xx] = (tmp_across,tmp_side)
            heapq.heappush(Q,(tmp_across,tmp_side,yy,xx))


            
    

print(res[0],end=" ")
print(res[1])


    
    
    






