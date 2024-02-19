def DFS(L):
    global cnt
    if L > len(n):
        return
    elif L == len(n):
        for i in res:
            print(i,end='')
        cnt+=1
        print()
        return
    else:
        if int(n[L])== 0 :
            return
        if L!=len(n)-1 and int(n[L+1])==0:
            res.append(chr(int(n[L:L+2])+64))
            DFS(L+2)
            res.pop()
        else:
            if int(n[L]) >0  :
                res.append(chr(int(n[L])+64))
                DFS(L+1)
                res.pop()
            if int(n[L:L+2]) <27 :
                res.append(chr(int(n[L:L+2])+64))
                DFS(L+2)
                res.pop()


if __name__ == "__main__":
    n = input()
    res=[]
    cnt=0
    DFS(0)
    print(cnt)
    
#답안


def DFS(L,P):
    global cnt
    if L == n:
        cnt+=1
        for j in range(P):
            print(chr(res[j]+64),end='')
        print()
    else:
        for i in range(1,27):
            if code[L]==i:
                res[P]=i
                DFS(L+1,P+1)
            elif i >=10 and code[L] ==i//10 and code[L+1]==i%10: # 10의자리와 1의자리가 같은지 보는거
                res[P]=i
                DFS(L+2,P+1)


if __name__ == "__main__":
    code = list(map(int,input())) # 25114를 list로 받은거임
    n = len(code)
    code.insert(n,-1) # index가 넘어가는것을 방지
    res=[0]*(n+3)
    cnt=0
    DFS(0,0)
    print(cnt)