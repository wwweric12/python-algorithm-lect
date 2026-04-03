def solution(money):
    answer = 0
    len_money=len(money)

    dp=[[0,0] for _ in range(len_money)]
    dp2=[[0,0] for _ in range(len_money)]

    
    ## 무조건 첫번째 집 방문
    for i in range(2,len_money-1):
        dp[i][0] = max(dp[i-1][0],dp[i-1][1])
        dp[i][1] = dp[i-1][0]+money[i]
        
    


    
    ## 무조건 첫번째 집 방문하지 않음
    for i in range(1,len_money):
        dp2[i][0] = max(dp2[i-1][0],dp2[i-1][1])
        dp2[i][1] = dp2[i-1][0]+money[i]

    
   
    tmp = max(dp[len(money)-2])+money[0]
    tmp2 =max(dp2[len(money)-1])
    answer= max(tmp,tmp2)
    
    
    return answer