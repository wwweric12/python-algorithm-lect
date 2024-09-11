from collections import deque

n, m = map(int, input().split())
lst = [list(map(int, input())) for _ in range(n)]  # 지도 입력

dy = [-1, 0, 0, 1]
dx = [0, 1, -1, 0]

res = [[0] * m for _ in range(n)]
area_size = {}
area_map = [[-1] * m for _ in range(n)]
area_id = 0

def bfs(a, b, area_id):
    q = deque()
    q.append((a, b))
    area_map[a][b] = area_id
    size = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < m and lst[xx][yy] == 0 and area_map[xx][yy] == -1:
                area_map[xx][yy] = area_id
                q.append((xx, yy))
                size += 1
    return size

for i in range(n):
    for j in range(m):
        if lst[i][j] == 0 and area_map[i][j] == -1:
            area_size[area_id] = bfs(i, j, area_id)
            area_id += 1

for i in range(n):
    for j in range(m):
        if lst[i][j] == 1:
            adj_areas = set()  
            for k in range(4):
                xx = i + dx[k]
                yy = j + dy[k]
                if 0 <= xx < n and 0 <= yy < m and area_map[xx][yy] != -1:
                    adj_areas.add(area_map[xx][yy])
            count = 1
            for area in adj_areas:
                count += area_size[area]
            res[i][j] = count % 10 

for i in range(n):
    for j in range(m):
        print(res[i][j],end='')
    print()    
    

