def solution(n, results):
    answer = 0
    graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
    
    for result in results:
        win, lose = result
        graph[win][lose] = 1
        graph[lose][win] = -1
        
    
    for i in range(1,n+1):
        for k in range(1,n+1):
            for j in range(1,n+1):
                if graph[i][k] ==1 and graph[k][j] ==1 :
                    graph[i][j] = 1
                    graph[j][i] = -1
                elif graph[i][k] ==-1 and graph[k][j] ==-1 : 
                    graph[i][j]=-1
                    graph[j][i] = 1
    
    
    
    for node in range(1,n+1):
        for j in range(1,n+1):
            if node != j:
                if graph[node][j] !=0:
                    continue
                break
        else:
            answer+=1
                
            
        
    
        
        
    
    return answer