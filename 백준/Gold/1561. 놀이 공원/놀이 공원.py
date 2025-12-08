## n이 20억이라 무조건 이진탐색인데
## 운행시간을 기준으로 해야할거 같은데 




n, m = map(int,input().split())
lst = list(map(int,input().split()))



if n<= m :
    print(n)
    
else:

    n-=m

    def check(value):
        cnt= 0
        
        for i in lst:
            cnt+= value//i
            
        return cnt 



    lt = 0
    rt = n*min(lst)
    v = 0



    while lt < rt :
        mid = (lt+rt)//2 
        cnt = check(mid)
        
        if cnt >= n:
            rt = mid
        elif cnt < n:
            lt = mid+1

    
  
    cnt = check(lt)


    for i in range(m-1,-1,-1):
        if lt% lst[i] == 0:
            if cnt == n:
                print(i+1)
                break
            else:
                cnt-=1



 
        
    