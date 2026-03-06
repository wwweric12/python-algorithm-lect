# 1 ≤ board의 행의 길이 (= N) ≤ 1,000
# 1 ≤ board의 열의 길이 (= M) ≤ 1,000
# 1 ≤ board의 원소 (각 건물의 내구도) ≤ 1,000
# 1 ≤ skill의 행의 길이 ≤ 250,000
# skill의 열의 길이 = 6
# skill의 각 행은 [type, r1, c1, r2, c2, degree]형태를 가지고 있습니다.

    ## 문제는 for문을 안돌면서 반영하는 방법이 뭐냐 인건데...
    ## skill이 25만이라 따로 돌아야함 
    ## 이거를 어떻게 반영할 수 있을까?
    
def solution(board, skill):
    answer = 0
    
    row_length = len(board)
    col_length = len(board[0])
    n_board = [[0 for _ in range(col_length+1)] for _ in range(row_length+1)]  

    
    for sk in skill:
                
        type, r1, c1, r2, c2, degree   =  sk
        if type ==1:
            n_board[r1][c1]-=degree
            n_board[r2+1][c2+1]-=degree
            n_board[r1][c2+1]+=degree
            n_board[r2+1][c1]+=degree
            
        else:
            n_board[r1][c1]+=degree
            n_board[r2+1][c2+1]+=degree
            n_board[r1][c2+1]-=degree
            n_board[r2+1][c1]-=degree

            
    for i in range(row_length+1):
        for j in range(col_length):
            n_board[i][j+1] += n_board[i][j]
    
   
    for i in range(col_length+1):
        for j in range(row_length):
            n_board[j+1][i] += n_board[j][i]
    
  
    
    
    for i in range(row_length):
        for j in range(col_length):
            
            if board[i][j] + n_board[i][j] <=0:
                
                answer+=1
                
    
    
    return row_length*col_length-answer