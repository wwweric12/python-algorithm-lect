import sys
def DFS(L):
    global res,lst
    if L == n:
        k=lst.copy() # 리스트를 변경해줘야되서 이전꺼를 기억해야 되기때문에 copy
        while len(lst) !=1:
            # lst를 돌면서 다더해주고 하나 남았을때 그만둠
            for i in range(len(lst)-1): 
                lst[i]=lst[i]+lst[i+1]
            lst.pop()   #lst를 마지막에 한개만 남기기위해 pop 
        res=lst[0] # 다더한겂
        if f == res:
            for i in k:
                print(i, end=' ')
            sys.exit(0)
        lst=k.copy() # 기존 lst는 한개만남아서 다시 사용해야 되서 k를 copy
        
    else:
        for i in range(1,n+1): # 중복한걸 빼기위해
            if ch[i]==0:
                ch[i]=1
                lst[L]=i
                DFS(L+1)
                ch[i]=0
         


if __name__ == "__main__":
    n, f = map(int,input().split())
    lst=[0]*n
    ch=[0]*(n+1)
    res=0
    DFS(0)
    
    
    
#답안

import sys

def DFS(L,sum):
    if sum >f:
        return
    if L == n and sum ==f:
        for x in p:
            print(x, end=' ')
        sys.exit(0)
    else:
        for i in range(1,n+1):
            if ch[i]==0:
                ch[i]=1
                p[L]=i
                DFS(L+1,sum+p[L]*b[L])
                ch[i]=0
                
        

if __name__ == "__main__":
    n, f = map(int,input().split())
    p=[0]*n #순열만듬
    b=[1]*n #무엇을 곱할지 이항계수
    ch=[0]*(n+1) # 순열중복방지
    for i in range(1,n):
        b[i]=b[i-1]*(n-i)//i # combination(조합) //은 소수점없애기위해서
    DFS(0,0)
    