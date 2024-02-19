res=0
n= int(input())
mid= n//2
lst = []
for i in range(n):
    k=list(map(int,input().split()))
    if i <= mid:
        res+=sum(k[mid-i:mid+i+1])
    else:
        res+=sum(k[mid-n+i+1:mid+n-i])
print(res)        

#답안
# 가장 가운데에서 상,하,좌,우 방향으로 BFS하는거임

from collections import deque

dx= [-1,0,1,0] # 상 하 좌 우
dy= [0,1,0,-1]
n= int(input())
a = [list(map(int,input().split())) for _ in range(n)]
ch = [[0]* n for _ in range(n)] #체크 배열 방문 여부
sum = 0
Q= deque()
ch[n//2][n//2]=1 # 중앙지점 
sum += a[n//2][n//2] 
Q.append((n//2),(n//2))
L=0
while True:
    if L ==n :
        break
    size= len(Q)
    for i in range(size):
        tmp = Q.popleft()
        for j in range(4):
            x = tmp[0]+dx[j]
            y = tmp[1]+dy[j]
            if ch[x][y] ==0:
                sum+=a[x][y]
                ch[x][y]=1
                Q.append((x,y))
    L+=1
print(sum)
        
    
    
    
    
