import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
v = int(input())

ch=[[] for _ in range(v+1)]

max_value=0
for _ in range(v):
    tmp =list(map(int,input().split()))
    index=1
    while True:   
        if tmp[index]==-1:
            break 
        ch[tmp[0]].append([tmp[index],tmp[index+1]])
        index+=2
        
def DFS(L,sum_value):
    global max_value, far_value
    if sum_value > max_value:
        max_value =sum_value
        far_value =L
    for i in ch[L]:
        if ch_index[i[0]]==0:
            ch_index[i[0]]=1
            DFS(i[0],sum_value+i[1])
    
    
ch_index=[0]*(v+1)
far_value=1
ch_index[1]=1
DFS(1,0)

ch_index=[0]*(v+1)
ch_index[far_value]=1
DFS(far_value,0)





print(max_value)