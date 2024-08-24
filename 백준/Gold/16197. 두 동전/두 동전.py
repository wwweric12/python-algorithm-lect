import sys
from collections import deque

n , m = map(int,input().split())

lst=[]
coin_index=[]


dx=[-1,0,0,1]
dy=[0,1,-1,0]

Q=deque()

for _ in range(n):
    tmp=list(input())
    lst.append(tmp)

for i in range(n):
    for j in range(m):
        if lst[i][j]=='o':
            coin_index.append([i,j])


Q.append([coin_index,0])            
prev_list=set()


while Q:
    coins,cnt= Q.popleft()
    
    if cnt >=10:
            print(-1)
            sys.exit()
            
    for i in range(4):
        tmp_coins=[]        
        out_of_bounds_count = 0
        for coin in range(2):
            y=coins[coin][0]+dy[i]
            x=coins[coin][1]+dx[i]
            if y < 0  or y >=n or x <0 or x >= m:
                out_of_bounds_count += 1
            else:
                if lst[y][x]=="#":
                    y=coins[coin][0]
                    x=coins[coin][1]
                tmp_coins.append([y,x])
        if out_of_bounds_count ==2:
            continue
        elif out_of_bounds_count ==1:
            print(cnt+1)
            sys.exit()
        else:
            if tmp_coins[0] == tmp_coins[1]:
                continue
                
            new_state = (tuple(tmp_coins[0]), tuple(tmp_coins[1]))
            if new_state not in prev_list:
                prev_list.add(new_state)
                Q.append((tmp_coins, cnt + 1))


            
else:   
    print(-1)
                    
    
