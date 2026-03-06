import sys
input = sys.stdin.readline

n, m = map(int,input().split())

lst=[]

for _ in range(n):
    tmp = list(map(int,input().split()))
    lst.append(tmp)


sum_lst=[[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    sum_lst[i][0] = lst[i][0]
    for j in range(n-1):

        sum_lst[i][j+1]+=(sum_lst[i][j]+lst[i][j+1])


for i in range(n):
    for j in range(n-1):
        sum_lst[j+1][i]+=sum_lst[j][i]


for _ in range(m):
    y1,x1, y2,x2 = map(int,input().split())
    res= sum_lst[y2-1][x2-1]
    if x1 == x2 and y1 == y2:
        print(lst[y1-1][x1-1])
        continue
    if x1!=1 :
        res -= sum_lst[y2-1][x1-2]
    if y1 != 1:
        res -= sum_lst[y1-2][x2-1]
    if x1 != 1 and y1 !=1:

        res +=sum_lst[y1-2][x1-2]

    print(res )

    
    
    
    

    
