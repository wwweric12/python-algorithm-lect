import sys
input = sys.stdin.readline
def DFS(l,sum):
    global res
    if sum >c:
        return
    if l == n:
        if sum >res:
            res= sum
    else:
        DFS(l+1,sum+lst[l])
        DFS(l+1,sum)

 

if __name__ == "__main__": 
    c,n=map(int,input().split()) 
    lst=[]
    res=0
    for _ in range(n):
        k=int(input())
        lst.append(k)
    DFS(0,0)
    print(res)

#답안


def DFS(L,sum,tsum):
    global result
    if sum+(total-tsum)< result:  # 지금까지 판단한값에다가 이제 남은값들을 더했을때 result보다 작게되면 더이상 판단안해도되서 미리 커트
        return
    if sum > c:
        return
    if L == n:
        if sum > result:
            result=sum
    else:
        DFS(L+1,sum+a[L],tsum+a[L])
        DFS(L+1,sum,tsum+a[L])

if __name__ == "__main__": 
    c,n=map(int,input().split())
    a=[0]*n 
    result = -214700000
    for i in range(n):
        a[i]= int(input())
    total =sum(a)
    DFS(0,0,0)
    

