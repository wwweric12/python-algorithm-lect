#DFS 깊이우선 탐색 왼쪽으로 계속 파고들어가는것
#BFS 넓이우선 탐색  레벨 탐색 

#전위순회 부 왼 오
#중위순회 왼 부 오 
#전위순회 왼 오 부 


def DFS(v):
    if  v>7:
        return
    else:
        #전위순회
        # print(v)
        # DFS(v*2)
        # DFS(v*2+1)
        
        #중위 순회
        # DFS(v*2)
        # print(v)
        # DFS(v*2+1)
        
        #후위 순회
        DFS(v*2)
        DFS(v*2+1)
        print(v)



if __name__ =="__main__":
    DFS(1)