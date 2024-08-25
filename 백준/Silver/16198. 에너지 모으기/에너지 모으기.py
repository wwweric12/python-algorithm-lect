n=int(input())
energe_lst=list(map(int,input().split()))
ch=[0 for _ in range(n)]

max_value=0
def DFS(L,sum_value):
    global max_value
    if L == n-2:
        max_value=max(max_value,sum_value)
        return
    else:
        for i in range(1,n-1):
            if ch[i]==0:
                ch[i]=1
                right=1
                while ch[i+right]!=0:
                    right+=1
                left=1
                while ch[i-left]!=0:
                    left+=1
                DFS(L+1,sum_value+(energe_lst[i-left]*energe_lst[i+right]))
                ch[i]=0

DFS(0,0)
print(max_value)

