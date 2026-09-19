def solution(distance, rocks, n):
    answer = 0
    
    rocks.append(0)
    rocks.append(distance)
    rocks.sort()
    cnt_rocks=len(rocks)
    dis = []
    
    left = 0
    right = distance
    
    for i in range(cnt_rocks-1):
        dis.append(rocks[i+1] - rocks[i])
    
    def check(value):
        nonlocal dis
        tmp =0
        cnt = 0
        for k in dis:
            tmp+=k
            if tmp <value: ## 최소길이보다 작은경우 
                cnt+=1
            else:
                tmp = 0
        return cnt            
    
    
    
    while left<=right:
        mid = (left + right)//2
        res = check(mid)
        if res <= n : 
            answer = mid 
            left=mid+1
        else:
            right=mid-1
        

        
        
        
    
    return answer