import heapq

n, m = map(int,input().split())
lst=[]

start=[]

for i in range(n):
    tmp = list(input())
    for j in range(m):
        if tmp[j] == '0':
            start=[i,j]
    lst.append(tmp)


key_to_num ={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5}
moon_to_num={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5} 

## heapq+ BFS로 움직여야할거같은데 
## 하지만 갔던곳도 갈 수 있어야함 열쇠가 있기때문에 
## 어떻게 해야할까
## 움직임마다 visited를 할 수는 없을거같은데 
## 열쇠를 먹으면 visited초기화 

dx=[-1,0,0,1]
dy=[0,1,-1,0]


visited={i:[]for i in range(2**6)}

visited[0].append((start[0],start[1]))



Q =[]
heapq.heappush(Q,(0,start[0],start[1],0))

res= -1
while Q:
    step,start_x,start_y,key = heapq.heappop(Q)
    if lst[start_x][start_y]=="1":
        res= step
        break
    for i in range(4):
        xx= start_x+dx[i]    
        yy= start_y+dy[i]
        if 0<=xx <n and 0<=yy<m and not (xx,yy) in visited[key] and lst[xx][yy] !="#":
            if lst[xx][yy]=="a" or  lst[xx][yy] == "b"or lst[xx][yy] == "c" or lst[xx][yy] == "d"or lst[xx][yy] == "e" or lst[xx][yy] == "f":
                new_key = key| 1<<key_to_num[lst[xx][yy]]
                visited[new_key].append((xx,yy))
                heapq.heappush(Q,(step+1,xx,yy,new_key))
                
            elif lst[xx][yy]=="A" or  lst[xx][yy] == "B"or lst[xx][yy] == "C" or lst[xx][yy] == "D"or lst[xx][yy] == "E" or lst[xx][yy] == "F":
                if key & 1<<moon_to_num[lst[xx][yy]]:
                    visited[key].append((xx,yy))
                    heapq.heappush(Q,(step+1,xx,yy,key)) 
            else:
                visited[key].append((xx,yy))
                heapq.heappush(Q,(step+1,xx,yy,key)) 
    
                
            
print(res)            
    





