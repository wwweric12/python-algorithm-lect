n=int(input())

res=0
cnt=0
def DFS(res,cnt,n):
    k=n
    while n//2 >0:
        n//=2
        cnt += 1    
    res+=1*10**cnt  
    n = k-2**cnt  
    if n> 0:
        cnt=0
        res = DFS(res,cnt,n)
    elif n == 1:
        res+=1
    return res 



print(DFS(res,cnt,n))

#답안


def DFS(x): #재귀함수 깊이우선탐색
    if x == 0:
        return
    else:
        DFS(x//2)
        print(x%2, end='')


if __name__ == "__main__":
    n= int(input())
    DFS(n)
