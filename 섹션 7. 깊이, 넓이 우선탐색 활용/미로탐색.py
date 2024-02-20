def DFS(s):
    global cnt
    if s== (6,6):
        cnt+=1
        return 
    else:
        for i in range(4):
            x= s[0]+dx[i]
            y= s[1]+dy[i]
            if 0<=x<=6 and 0<=y<=6  and lst[x][y]==0:
                lst[x][y]=1
                DFS((x,y))
                lst[x][y]=0
                



if __name__ == "__main__":
    lst=[]
    for _ in range(7):
        lst.append(list(map(int,input().split())))
    lst[0][0]=1
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    cnt=0
    DFS((0,0))
    print(cnt)

#답안은 풀이와 동일
