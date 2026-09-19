def solution(k, dungeons):
    answer = -1
    len_dun =len(dungeons)
    
    ch=[0 for _ in range(k+1)]
    
    def DFS(L,value,hp):
        nonlocal answer
        if L == len(dungeons):
            answer = max(answer,value)
            
        for i in range(len_dun):
            if ch[i] == 0:
                ch[i] = 1
                if hp >= dungeons[i][0]:
                    DFS(L+1,value+1,hp-dungeons[i][1])
                DFS(L+1,value,hp)    
                ch[i] = 0
            

    DFS(0,0,k)

    return answer