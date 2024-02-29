n= int(input())

lst = [list(map(int,input().split())) for _ in range(n)]
dx=[1,0]

ch = [[0]*n for _ in range(n)]
ch[0][0] = lst[0][0]


for i in range(n):
    for j in range(n):
        if i>0 and j>0 :
            if ch[i-1][j] > ch[i][j-1]:
                ch[i][j] = ch[i][j-1] + lst[i][j]
            else:
                ch[i][j] = ch[i-1][j] + lst[i][j]
        elif i ==0  and j>0:
            ch[i][j]= ch[i][j-1]+lst[i][j]
        else: 
            ch[i][j]= ch[i-1][j]+lst[i][j]            

print(ch[n-1][n-1])

            
#답안은 풀이와 동일 


