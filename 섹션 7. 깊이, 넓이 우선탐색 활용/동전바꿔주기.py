import sys
input = sys.stdin.readline
def DFS(L,s):
    global cnt
    if s == T:
        cnt+=1
        return 
    elif s<T :
            for i in range(L,k):
                if lst[i][0] > T-s :
                    return
                if ch[i] < lst[i][1]:
                    ch[i]+=1
                    DFS(i,s+lst[i][0])  
                    ch[i]-=1
    else:
        return
        
                    
if __name__ == "__main__":
    T = int(input())
    k = int(input())
    cnt=0
    lst=[]
    ch=[0]*k
    for _ in range(k):
        a, b = map(int,input().split())
        lst.append((a,b))
    lst.sort(key= lambda x: x[0])
    DFS(0,0)
    print(cnt)
    

#답안 
# 5원 0 1 2 3 개씩 
# 10원 0 1 2 개씩 ... 이런식으로 
import sys
input = sys.stdin.readline

def DFS(L,s):
    global cnt
    if s >T :
        return
    if L==k:
        if s == T:
            cnt+=1
    else:
        for i in range(cn[L]+1):
            if cv[L]*i > T-s :
                return
            DFS(L+1,s+cv[L]*i)

        
                    
if __name__ == "__main__":
    T = int(input())
    k = int(input())
    cnt=0
    cv = []
    cn = []
    for _ in range(k):
        a, b = map(int,input().split())
        cv.append(a)
        cn.append(b)
    DFS(0,0)
    print(cnt)
    