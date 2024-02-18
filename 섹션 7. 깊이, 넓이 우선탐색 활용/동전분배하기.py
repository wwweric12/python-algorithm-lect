def DFS(L):
    global t
    if L == n:
        if t > max(res)-min(res) and len(set(res)) == 3:
            t=max(res)-min(res)
        return
    else:
        for i in range(3):
            res[i]=res[i]+lst[L]
            DFS(L+1)
            res[i]=res[i]-lst[L]
        

if __name__ == "__main__":
    n = int(input())
    lst=[]
    res=[0]*3
    t=2147000
    for _ in range(n):
        k = int(input())
        lst.append(k)
    DFS(0)
    print(t)
    
#답안은 풀이와 동일 



