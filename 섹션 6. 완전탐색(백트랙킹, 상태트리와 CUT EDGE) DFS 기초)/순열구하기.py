def DFS(v):
    global cnt
    if v == m:
        if len(set(ch)) == len(ch):
            for i in range(m):
                print(ch[i], end=' ')
            cnt+=1
            print()
    else:
        for i in range(1,n+1):
            ch[v]=i
            DFS(v+1)


if __name__ == "__main__":
    n, m = map(int,input().split())
    cnt=0
    ch=[0]*m
    DFS(0)
    print(cnt)

#답안

def DFS(L):
    global cnt
    if L ==m:
        for j in range(L):
            print(res[j], end=' ')
        print()
        cnt+=1
    else:
        for i in range(1,n+1):
            if ch[i]==0:
                ch[i]=1
                res[L]=i
                DFS(L+1)
                ch[i]=0 #다시 돌려주는거임 




if __name__ == "__main__":
    n, m = map(int,input().split())
    res=[0]*n #출력할거 
    ch[0]*(n+1) # 0인자리에만 출력하는거임 기존에 추가되서 중복안시키게 하기위해서 
    cnt=0
    DFS(0)
    print(cnt)