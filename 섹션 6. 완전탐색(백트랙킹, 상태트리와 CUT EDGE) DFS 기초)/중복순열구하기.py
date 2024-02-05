

#답안 

import sys
input = sys.stdin.readline
# s =input().rstrip() 문자열읽을때는 이렇게 이유는 줄바꿈기호까지 읽어서 


def DFS(L):
    global  cnt
    if L == m:
        for i in res:
            print(i,end=' ')
        cnt+=1
        print()

    else:
        for i in range(1,n+1):
            res[L]=i
            DFS(L+1)
    
if __name__ == "__main__":
    n,m=map(int,input().split())
    res=[0]*m
    cnt=0
    DFS(0)
    print(cnt)