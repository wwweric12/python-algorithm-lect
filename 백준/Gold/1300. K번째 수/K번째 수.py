n = int(input())
k = int(input())


# 1부터 n까지 n번 더한값들 
# 1  2  3  4  5
# 2  4  6  8  10
# 3  6  9  12 15
# 4  8  12 16 20
# 5  10 15 20 25

# N 은 10**5 까지 , K는 10**9 또는 10**10 보다 작거나 같은 자연수 
# N*N이니까 10**10임 전부 계산하면
# 그러면 계산을 하지말고 k번째를 찾아야하는 방법이 있어야하는데 

## 값을 정해놓고 찾기

array=[]

def binary_search(start, end, func):
    if start > end :
        return None
    mid = (start+end)//2
    cnt=func(mid)
    if cnt >= k:
        array.append(mid)
        return binary_search(start,mid-1,func)
    elif cnt < k:
        return binary_search(mid+1,end,func)
    
        
    


def sum_cnt(value):
    cnt = 0
    for i in range(1,n+1):
        cnt += min(value // i,n)
    return cnt  
        
    
binary_search(0,n*n,sum_cnt)
print(min(array))