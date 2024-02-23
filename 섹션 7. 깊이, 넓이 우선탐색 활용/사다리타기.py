
def DFS(x,y):
    if y ==0:
        print(x)
        return
    else:
        for j in range(3):
            xx = x+dx[j]
            yy = y+dy[j]
            if 0<=xx <10 and 0<=yy<10 and lst[yy][xx] == 1 and ch[yy][xx]==0:
                ch[yy][xx]=1
                DFS(xx,yy)
                break



if __name__ == "__main__":
    dx=[-1,1,0]
    dy=[0,0,-1]
    ch=[[0]*10 for _ in range(10)]
    lst=[list(map(int,input().split())) for _ in range(10)]
    for i in range(10):
        if lst[9][i]==2:
            DFS(i,9)
            break
        
#답안



def DFS(x,y):
    ch[x][y]=1
    if x ==0:
        print(y)
        return
    else:
        if y-1>=0 and board[x][y-1] ==1 and ch[x][y-1]==0:#왼쪽
            DFS(x,y-1)
        elif y+1>=0 and board[x][y+1] ==1 and ch[x][y+1]==0: # 오른쪽
            DFS(x,y+1)
        else: #위로
            DFS(x-1,y)


if __name__ == "__main__":
    ch=[[0]*10 for _ in range(10)]
    board=[list(map(int,input().split())) for _ in range(10)]
    for y in range(10):
        if board[9][y]==2:
            DFS(9,y)
            break
        