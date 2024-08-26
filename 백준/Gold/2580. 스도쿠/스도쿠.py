import sys
input= sys.stdin.readline

sudoku=[]
empty=[]


for i in range(9):
    sudoku.append(list(map(int,input().split())))
    for j in range(9):
        if sudoku[i][j]==0:
            empty.append([i,j])


def check(x,y,num):
    xx = (x//3)*3
    yy= (y//3)*3
    for i in range(9):
        if sudoku[x][i]==num or sudoku[i][y]==num:
            return False
        if sudoku[xx+i//3][yy+i%3]==num:
            return False
    return True

    

            
            


def DFS(L):
    if L ==len(empty):
        for row in sudoku:
            for number in row:
                print(number,end=' ')
            print()        
        sys.exit()
    else:
        x,y =empty[L]
        for num in range(1, 10):
            if check(x, y, num):
                sudoku[x][y] = num
                DFS(L + 1)
                sudoku[x][y] = 0

DFS(0)