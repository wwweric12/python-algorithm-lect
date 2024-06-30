import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(node, color):
    global state
    ch[node] = color
    for i in lst[node]:
        if ch[i] == 0:  # 아직 방문하지 않은 경우
            DFS(i, 3 - color)  # 다른 색으로 색칠
        elif ch[i] == color:  # 인접한 노드가 같은 색인 경우
            state = True
            return

k = int(input())
for _ in range(k):
    v, e = map(int, input().split())
    lst = [[] for _ in range(v + 1)]
    ch = [0] * (v + 1)
    state = False

    for i in range(e):
        a, b = map(int, input().split())
        lst[a].append(b)
        lst[b].append(a)

    for i in range(1, v + 1):
        if ch[i] == 0:  # 방문하지 않은 경우에만 DFS 시작
            DFS(i, 1)

    if state:
        print("NO")
    else:
        print("YES")
