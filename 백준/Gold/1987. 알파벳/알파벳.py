import sys
input = sys.stdin.readline

r,c = map(int,input().split())
lst=[]
ch_alpha=[0 for _ in range(26)]
for _ in range(r):
    lst.append(list(input()))


dx=[-1,0,0,1]
dy=[0,1,-1,0]
max_value=0
ch_alpha[ord(lst[0][0])-65]=1

def alpha_DFS(x,y,cnt):
    global max_value
    if cnt >max_value:
        max_value=cnt
    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]
        if 0 <= xx <r and 0<= yy <c and ch_alpha[ord(lst[xx][yy])-65]==0:
            ch_alpha[ord(lst[xx][yy])-65]+=1
            alpha_DFS(xx,yy,cnt+1)
            ch_alpha[ord(lst[xx][yy])-65]-=1
            
alpha_DFS(0,0,1)

print(max_value)
            