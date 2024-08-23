n = int(input())
lst = list(map(int,input().split()))

res_index=[0]*2000000

def DFS(L,sum_value):
    if L ==n:
        res_index[sum_value]=1
        return
    else:
        DFS(L+1,sum_value+lst[L])
        DFS(L+1,sum_value)
                

DFS(0,0)

for i in range(1,2000001):
    if res_index[i]==0:
        print(i)
        break
            
    



