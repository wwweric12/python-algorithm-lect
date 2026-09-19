#해당 숫자  나누기 해당 숫자로 1을 구할 수 있고
#숫자르 붙이면 11  그래서 1, 11, 111 이런순서인데
#(55+55)/5 -> 22 

def solution(N, number):
    answer = 0

    dp= [set() for _ in range(9)]
    
    for i in range(1,9):
        dp[i].add(int(str(N)*i))
        
        for j in range(1,i):
            for k in dp[j]:
                for t in dp[i-j]:
                    dp[i].add(k+j)
                    dp[i].add(k*j)
                    dp[i].add(k-j)
                    if j !=0:
                        dp[i].add(k//j)
        
        if number in dp[i]:
            return i
                    
                    
        
    
    return answer