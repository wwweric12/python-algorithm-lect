def DFS(L,sum,l):
    global res
    if L > n:
        if sum-l > res:
            res=sum-l
        return 
    elif L == n:
        if sum > res:
            res=sum
        return 
    else:
        for i in range(L,n):    
            DFS(i+time[i],sum+money[i],money[i])

            



if __name__ == "__main__":
    n = int(input())
    time=[]
    money=[]
    res=0
    for _ in range(n):
        a ,b = map(int,input().split())
        time.append(a)
        money.append(b)
    DFS(0,0,0)
    print(res)
    
#답안


def DFS(L,sum):
    global res
    if L ==n+1:
        if sum >res:
            res =sum
        else:
            if L+T[L] <= n+1:
                DFS(L+T[L],sum+P[L])
            DFS(L+1,sum)   
    

if __name__ == "__main__":
    n = int(input())
    T=list()
    P=list()
    res=-21470000
    for _ in range(n):
        a ,b = map(int,input().split())
        T.append(a)
        P.append(b)
    T.insert(0,0) #index를 날짜로 사용하기위해 0번 index에 0 삽입
    P.insert(0,0)
    DFS(1,0)
    print(res)