import sys

input= sys.stdin.readline

n= int(input())
lst=[[0,0]for _ in range(n+1)]
ch=[[]for _ in range(n+1)]
location=[0]
root_ch=[0]*(n+1)
root=0
for _ in range(n):
    node ,left, right = map(int,input().split())
    root_ch[node]+=1
    if left !=-1:
        root_ch[left]+=1
    if right !=-1:
        root_ch[right]+=1
    lst[node][0]=left
    lst[node][1]=right

for i in range(1,n+1):
    if root_ch[i]==1:
        root=i
        break

max_layer=0
def pre_root(root,cnt):
    global max_layer
    if root !=-1:
        ch[cnt].append(root)
        pre_root(lst[root][0],cnt+1)
        location.append(root)
        pre_root(lst[root][1],cnt+1)
        max_layer=max(max_layer,cnt)
        
pre_root(root,0)

max_value=0
max_index=0
for i in range(1,max_layer+1):
    if location.index(ch[i][-1])-location.index(ch[i][0]) > max_value:
        max_value =location.index(ch[i][-1])-location.index(ch[i][0])
        max_index=i
        

print(max_index+1,end=' ')
print(max_value+1)