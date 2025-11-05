from collections import deque

def solution(n, lighthouse):
    answer = 0
    graph = [[] for _ in range(n + 1)]
    degree = [0 for _ in range(n+1)]
    
    for a, b in lighthouse:
        graph[a].append(b)
        graph[b].append(a)
        degree[a] += 1
        degree[b] += 1

    is_lit = [0 for _ in range(n+1)]
    
    Q = deque([])
    for i in range(1, n + 1):
        if degree[i] == 1:
            Q.append(i)

    while Q:
        leaf = Q.popleft()
        if degree[leaf] == 0:
            continue
        degree[leaf] = 0
        parent = -1
        for node in graph[leaf]:
            if degree[node] > 0: 
                parent = node
                break
        
        if parent == -1:
            continue
    
        if is_lit[leaf] == 0:
            if is_lit[parent] == 0: 
                is_lit[parent] = 1  
                answer += 1
        
        degree[parent] -= 1
        

        if degree[parent] == 1:
            Q.append(parent)
            
    return answer