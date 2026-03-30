import sys, heapq

n, m = map(int, input().split())
lst = [list(input().strip()) for _ in range(n)]

if (m + n) % 2 != 0:
    print("NO SOLUTION")
    sys.exit()

cnt = 0
if lst[0][0] != "\\":
    cnt += 1

Q = []
heapq.heappush(Q, (cnt, 0, 0, "\\"))

# 3차원 배열: ch[y][x][0]은 "\" 상태 최소비용, ch[y][x][1]은 "/" 상태 최소비용
ch = [[[250001, 250001] for _ in range(m)] for _ in range(n)]
ch[0][0][0] = cnt

# "\" 타일일 때 갈 수 있는 6방향 (dy, dx, 필요한 모양)
# 순서: 좌상단, 상단, 좌측, 우하단, 하단, 우측
moves_back = [
    (-1, -1, "\\"), (-1, 0, "/"), (0, -1, "/"), 
    (1, 1, "\\"), (1, 0, "/"), (0, 1, "/")
]

# "/" 타일일 때 갈 수 있는 6방향 (dy, dx, 필요한 모양)
# 순서: 우상단, 상단, 우측, 좌하단, 하단, 좌측
moves_forward = [
    (-1, 1, "/"), (-1, 0, "\\"), (0, 1, "\\"), 
    (1, -1, "/"), (1, 0, "\\"), (0, -1, "\\")
]

while Q:
    count, y, x, prev = heapq.heappop(Q)

    # 도착 조건: 마지막 타일이고, 모양이 "\"로 배치되어 끝점에 닿았을 때
    if y == n - 1 and x == m - 1 and prev == "\\":
        print(count)
        sys.exit()
    
    # 이미 더 적은 비용으로 현재 모양(prev)을 만든 적 있으면 패스
    state_idx = 0 if prev == "\\" else 1
    if ch[y][x][state_idx] < count:
        continue

    # 현재 타일 모양에 따라 체크할 6방향 지정
    directions = moves_back if prev == "\\" else moves_forward

    for dy, dx, req_shape in directions:
        yy = y + dy
        xx = x + dx
        
        if 0 <= yy < n and 0 <= xx < m:
            next_state_idx = 0 if req_shape == "\\" else 1
            
            # 모양이 다르면 1회전, 같으면 0회전
            cost_add = 0 if lst[yy][xx] == req_shape else 1
            next_count = count + cost_add
            
            # 갱신될 때만 heapq에 넣음 (질문자님 코드의 else문 무한루프 문제 해결)
            if ch[yy][xx][next_state_idx] > next_count:
                ch[yy][xx][next_state_idx] = next_count
                heapq.heappush(Q, (next_count, yy, xx, req_shape))

print("NO SOLUTION")