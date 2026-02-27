import heapq
import sys

input = sys.stdin.readline


w, h = map(int,input().split())

lst=[]

for i in range(h):
    tmp=list(input())
    lst.append(tmp)


start = (0,0)

for i in range(h):
    for j in range(w):
        if lst[i][j] == "T":
            start = (i,j) 
            break


hq = []

dy=[-1,0,0,1]
dx=[0,-1,1,0]

visited = [[float('inf') for _ in range(w) ] for _ in range(h)]
visited_dir = [[[float('inf')] * 4 for _ in range(w)] for _ in range(h)]
visited[start[0]][start[1]] =0
res = -1

def check_possible(y,x,num,value):
    global res
    while True:
        y += dy[num]
        x += dx[num]
        if x<0 or x>=w  or  y<0  or y>=h or lst[y][x]== "H" or lst[y][x] =="T":
            return False, value, y, x 

        if visited_dir[y][x][num] <= value:
            return False, value, None, None
        visited_dir[y][x][num] = value 

        if lst[y][x] == "E":          
            if visited[y][x] > value :
                res = value 
                visited[y][x] = value 
            return False, value, y, x 

        if lst[y][x] == "R":
            if visited[y-dy[num]][x-dx[num]] <= value:
                return False, value ,y,x

            else:
                visited[y-dy[num]][x-dx[num]]= value
                return True, value, y-dy[num], x-dx[num] 

        value += int(lst[y][x])
        if res != -1 and res<= value:
            return False, value, None, None
        


for i in range(4):
    possible, value, y, x =check_possible(start[0],start[1],i,0)

    if possible:
        heapq.heappush(hq,(value,y,x))


while hq: 
    value, y,x  =heapq.heappop(hq)   
    if visited[y][x] < value:
        continue
    if res != -1 and res<= value:
        break
    for i in range(4):
        possible, nx_value, ny, nx =check_possible(y,x,i,value)

        if possible:
            heapq.heappush(hq,(nx_value,ny,nx))

print(res)
