def DFS(L,k):
    if L == m: 
        global res
        minV=24170000
        lv=0
        for i in range(n):
            for j in range(n):
                if lst[i][j] == 1:
                    for a in range(len(ch)):
                        if tl[a] == 1 :
                            tmp = abs(ch[a][0]-i)+abs(ch[a][1]-j)
                            if minV > tmp:
                                minV = tmp
                    lv+=minV
                    minV=24170000
        if res > lv:
            res=lv
        return


    else:
        for i in range(k,len(ch)):
            tl[i]=1
            DFS(L+1,i+1)
            tl[i]=0

                
                    


if __name__ =="__main__":
    n, m = map(int,input().split())
    res=24170000
    ch=[]
    lst=[list(map(int,input().split())) for _ in range(n)]
    for i in range(n):
            for j in range(n):
                if lst[i][j]==2:
                    ch.append((i,j))
    tl=[0]*len(ch)
    DFS(0,0)
    print(res)
    
                
    
    
# 답안

def DFS(L,s):
    global res
    if L == m: 
        sum=0 #도시의 피자거리
        for j in range(len(hs)):
            x1 =hs[j][0]
            y1 =hs[j][1]
            dis =2147000000
            for x in cb:
                x2 =pz[x][0]
                y2 =pz[x][1]
                dis =min(dis,abs(x1-x2)+abs(y1-y2)) # 최소값구하기
            sum+=dis
        if sum <res :
            res= sum
                

            
        return
    
    else:
        for i in range(s,len(pz)):
            cb[L]=i #이렇게 하면 index값으로 할 수 있다 
            DFS(L+1,i+1)
            

                
                    


if __name__ =="__main__":
    n, m = map(int,input().split())
    board=[list(map(int,input().split())) for _ in range(n)]
    hs=[] # 집의 좌표
    pz=[] # 피자집의 좌표
    cb=[0]*m # 살아남은 피자 조합
    res=2417000000

    for i in range(n):
            for j in range(n):
                if board[i][j]==1:
                    hs.append((i,j))
                if board[i][j]==2:
                    pz.append((i,j))
    DFS(0,0)
    print(res)