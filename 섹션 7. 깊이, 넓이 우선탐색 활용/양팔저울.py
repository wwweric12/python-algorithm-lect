def DFS(L,s):
    if L == k:
        if abs(s) not in a:
            a.append(abs(s))
        return
    else:
        DFS(L+1,s+lst[L])
        DFS(L+1,s)
        DFS(L+1,s-lst[L])
                    


if __name__ =="__main__":
    k = int(input())
    a=[]
    lst = list(map(int,input().split()))
    DFS(0,0)
    print(sum(lst)-(len(a)-1))

    
#답안


def DFS(L,sum):
    global res
    if L == n:
        if 0 < sum <=s: # -는 의미없음 어짜피 대칭구조라 생기게되어있음 
            res.add(sum) #set이라 append가 아니라 add
        return
    else:
        DFS(L+1,sum+G[L]) #추를 왼쪽
        DFS(L+1,sum-G[L]) #추를 오른쪽
        DFS(L+1,sum) #추를 사용하지않음
                    


if __name__ =="__main__":
    n = int(input())
    G = list(map(int,input().split()))
    s= sum(G)
    res = set()
    DFS(0,0)
    print(s -len(res))
    