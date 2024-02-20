def DFS(x,y):
    global cnt
    if x ==max_index[0] and y ==max_index[1]:
        cnt+=1
        return
    else:
        for i in range(4):
            xx = x+dx[i]
            yy = y+dy[i]
            if 0<= xx < n and 0<= yy < n  and lst[x][y] < lst[xx][yy]:
                DFS(xx,yy)

if __name__ == "__main__":
    n = int(input())
    lst=[]
    minv=2147000
    maxv= -2147000
    min_index =(0,0)
    max_index =(0,0)
    for i in range(n):
        k =list(map(int,input().split()))
        a=min(k)
        b=max(k)
        if minv > a :
            minv=a
            min_index = (i,k.index(a))
        if maxv < b :
            maxv=b
            max_index = (i,k.index(b)) 
        lst.append(k)
    dx = [-1,0,0,1]
    dy = [0,1,-1,0]
    cnt =0
    DFS(min_index[0],min_index[1])
    print(cnt)
    
#답안은 풀이와 동일 
