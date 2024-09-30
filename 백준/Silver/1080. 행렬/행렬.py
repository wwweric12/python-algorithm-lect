import sys
input = sys.stdin.readline
n, m = map(int,input().split())

a_lst=[]
b_lst=[]

for i in range(n):
    a_lst.append(list(map(int,input().strip())))
for i in range(n):
    b_lst.append(list(map(int,input().strip())))
    

dx=[-1,-1,-1,0,0,0,1,1,1]
dy=[0,-1,1,0,-1,1,0,-1,1]
cnt=0

def change(row,col):
    for i in range(9):
        n_row= row+dx[i]
        n_col =col+dy[i]
        a_lst[n_row][n_col]=(a_lst[n_row][n_col]+1)%2



if n<3 or m <3 :
    if a_lst !=b_lst:
        print(-1)
    else:
        print(0)
    sys.exit()
else:
    for i in range(n-2):
        for j in range(m-2):
            if a_lst[i][j] != b_lst[i][j]:
                change(i+1,j+1)
                cnt+=1
         
for i in range(n):
    for j in range(m):
        if a_lst[i][j] !=b_lst[i][j]:
            print(-1)
            sys.exit()
                        
print(cnt)

