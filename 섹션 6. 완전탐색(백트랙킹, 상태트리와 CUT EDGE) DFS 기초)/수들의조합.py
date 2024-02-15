def DFS(L,s):
    global cnt
    if L == k:
        if sum(res)%m == 0:  #조합의 합이 정수m의 배수일때 cnt+=1
            cnt+=1
        else:
            return
    else:
        for i in range(s,n):
            if ch[i]==0:
                ch[i]=1
                res.append(lst[i]) #lst에 담아놨던 값을 res에 하나씩 담기
                DFS(L+1,i) # 조합이기 때문에 i값을 넘김으로써 자기보다 낮은 Index값은 취급못하도록
                ch[i]=0
                res.pop()
                
        


if __name__ == "__main__":
    n , k = map(int,input().split())
    lst = list(map(int,input().split()))
    m = int(input())
    cnt=0
    ch =[0]*n
    res=[]
    DFS(0,0)
    print(cnt)

#답안
def DFS(L, s, sum):
    global cnt
    if L == k:
        if sum% m ==0:
            cnt+=1
    else:
        for i in range(s,n):
            DFS(L+1,i+1,sum+a[i])

if __name__ == "__main__":
    n , k = map(int,input().split())
    a = list(map(int,input().split()))
    m = int(input())
    cnt=0
    DFS(0,0,0)
    print(cnt)


#라이브러리를 사용해서 구현

import itertools as it

n , k = map(int,input().split())
a = list(map(int,input().split()))
m = int(input())
cnt=0
for x in it.combinations(a,k): # a라는 리스트에서 k개만 뽑는 조합을 튜플형태로 나옴
    if sum(x)%m ==0:
        cnt+=1
print(cnt)
