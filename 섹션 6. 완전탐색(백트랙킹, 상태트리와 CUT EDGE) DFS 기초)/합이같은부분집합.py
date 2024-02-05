def DFS(v):
    if v == n:
        s = 0
        k = 0
        for i in range(n):
            if ch[i]==1 :
                s+=lst[i] 
            else:
                k+=lst[i]
        return s==k
    else:
        ch[v]=1
        if DFS(v+1):
            return True
        ch[v]=0
        if DFS(v+1):
            return True
        
 
 
if __name__ == "__main__":
    n = int(input())
    lst=list(map(int,input().split()))
    ch=[0]*n
    if DFS(0):
        print("YES")
    else:
        print("NO")
        

#답안

import sys

def DFS(L,sum):
    if sum >total//2 : # 전체합의 반보다 커지면 어짜피 같아질 수 없기때문에 DFS를 할필요가없다 
        return 
    if L == n: # 종료지점
        if sum == (total-sum):
          print("YES")
          sys.exit(0)   #프로그램 종료
    else:
        DFS(L+1, sum+a[L])
        DFS(L+1, sum)
        
        
        
        

if __name__ == "__main__":
    n = int(input())
    a=list(map(int,input().split()))
    total = sum(a)
    DFS(0,0)