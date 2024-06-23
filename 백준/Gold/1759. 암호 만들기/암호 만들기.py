l,c = map(int,input().split())

lst=list(input().split())
lst.sort()


ch=[0]*c
res=[]

def condition(arr):
    lt=0
    rt=0
    for i in arr:
        if "a" == i or "e" == i or "i" == i or "o" == i or "u" == i:
            lt+=1
        else:
            rt+=1
    if lt>0 and rt >1:
        return True
        



def DFS(L,S):
    if L==l and condition(res):
        for i in res:
            print(i, end='')
        print()
        return 
    else:
        for i in range(S,c):
            if ch[i]==0:
                ch[i]=1
                res.append(lst[i])
                DFS(L+1,i)
                res.pop()
                ch[i]=0
            



DFS(0,0)























