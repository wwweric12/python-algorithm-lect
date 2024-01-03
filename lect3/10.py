lst=[]
for _ in range(9):
    lst.append(list(map(int,input("").split())))
    
dx=[0,0,0,1,1,1,2,2,2]
dy=[0,1,2,0,1,2,0,1,2]    
    

for i in range(9):
    if len(set(lst[i])) != 9 or sum(lst[i])!=55:
        print("NO")
        break
    if i%3==0:
        tmp=[]
        for k in range(9):
            tmp.append(lst[i+dx[k]][i+dy[k]])
        if len(set(tmp)) !=9 or sum(tmp) !=55 :
            print("NO")
            break



        


#답안

def check(a):
    ch1=[0]*10  #행 체크 
    ch2= [0]*10 # 열 체크 
    for j in range(9):
        ch1[a[i][j]]=1
        ch2[a[i][j]]=1
    if sum(ch1)!=9 or sum(ch2)!=9:
        return False
    for i in range(3):
        for j in range(3):
            ch3=[0]*10
            for k in range(3):
                for s in range(3):
                    ch3[a[i*3+k][j*3+s]]=1
            if sum(ch3) !=9:
                return False
    return True    
    
    
    
    
    
    
a=[list(map(int,input().split()))for _ in range(9)]
if check(a):
    print("YES")
else:
    print("NO")
    
    
    

sudoku = [list(map(int, input().split())) for i in range(9)]
answer = True

for i in range(9):
    if len(set(sudoku[i])) != 9:
        answer = False
        break
    if len(set(sudoku[i][j] for j in range(9))) != 9:
        answer = False
        break
    if len(set(sudoku[i//3*3][i%3*3:(i%3+1)*3] + sudoku[i//3*3+1][i%3*3:(i%3+1)*3] + sudoku[i//3*3+2][i%3*3:(i%3+1)*3])) != 9:
        answer = False
        break
    
if answer:
    print("YES")
else:
    print("NO")