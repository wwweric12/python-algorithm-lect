def solution(n, times):
    answer = 0
    left = 0
    right =  max(times)*n
    
    def check(mid):
        tmp = 0
        for time in times:
            tmp += mid//time
        return tmp
    
    while left <= right:
        mid = (left+right)//2
        tmp = check(mid)
        
        if tmp >= n:
            right = mid-1
        else:
            left=mid+1
    
    answer = left
    
    return answer