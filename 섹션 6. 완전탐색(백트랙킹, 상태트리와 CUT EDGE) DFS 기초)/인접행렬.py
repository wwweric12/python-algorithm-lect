n , m = map(int,input().split())
lst=[[0]*n for _ in range(n)]
for i in range(m):
    s,e,k = map(int,input().split())
    lst[s-1][e-1]=k
for i in range(n):
    for j in range(n):
        print(lst[i][j], end=' ')
    print()
        
#답안은 풀이와 동일 

