def DFS(v,sum):
    global cnt
    if v > cnt:
        return 
    elif sum > m:
        return
    elif sum ==m:
        if cnt >v :
            cnt =v
        return
    else:
        for i in range(n):
            DFS(v+1,sum+lst[i])
    

if __name__ == "__main__":
    n = int(input())
    lst= list(map(int,input().split()))
    lst.sort(reverse=True)
    m = int(input())
    cnt=10000
    DFS(0,0)
    print(cnt)

#답안과 동일 

