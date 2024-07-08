import sys
n,m =map(int,input().split())
lst=[]
for _ in range(n):
    s=input()
    tmp=[]
    for i in s: 
        tmp.append(i)
    lst.append(tmp)
ch=[[0 for _ in range(m)] for _ in range(n)]

dx=[1,0,0,-1]
dy=[0,1,-1,0]

def DFS(L,I,cnt,s_L,s_I):
    if L ==s_L and I==s_I and cnt>3:
        print("Yes")
        sys.exit()
    else:
        for i in range(4):
            y =L+dy[i]
            x= I+dx[i]
            if 0<= x <m and 0<= y<n and lst[L][I] ==lst[y][x] and ch[y][x]==0:
                ch[y][x]=1
                DFS(y,x,cnt+1,s_L,s_I)
                ch[y][x]=0
    

for i in range(n):
    for j in range(m):
        DFS(i,j,0,i,j)
            
print("No")
