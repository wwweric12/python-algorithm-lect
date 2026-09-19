#해당 숫자  나누기 해당 숫자로 1을 구할 수 있고
#숫자르 붙이면 11  그래서 1, 11, 111 이런순서인데
#(55+55)/5 -> 22 

def solution(N, number):
    answer = -1

    dp= [set() for _ in range(9)]
    
    for i in range(1,9):
        dp[i].add(int(str(N)*i))
        
        for j in range(1,i):
            for k in dp[j]:
                for t in dp[i-j]:
                    dp[i].add(k+t)
                    dp[i].add(k*t)
                    dp[i].add(k-t)
                    if t !=0:
                        dp[i].add(k//t)
        
        if number in dp[i]:
            if i >8:
                return -1
            return i
                    
                
        
    
    return answer