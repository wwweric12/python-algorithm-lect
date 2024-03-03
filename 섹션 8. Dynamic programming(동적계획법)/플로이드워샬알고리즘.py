n , m = map(int,input().split())

dy=[[21]*(n) for _ in range(n)]


for i in range(m):
    s ,d ,v = map(int,input().split())
    if dy[s-1][d-1] > v :
        dy[s-1][d-1]=v
        
a=0
while a!=n-1:
    a+=1
    for i in range(n):
        for j in range(n):
            if dy[i][j] != "M" and dy[i][a] != "M" and dy[a][j] != "M":
                dy[i][j]= min(dy[i][j],dy[i][a]+dy[a][j])
            if i == j :
                dy[i][j]=0
        
        
    
for k in dy:
    for s in k:
        if s == 21:
            print("M",end=' ')
        else:
            print(s,end=' ')
    print()
    

        
#답안 

if __name__ == "__main__":
    n , m = map(int,input().split())
    dis=[[5000]*(n+1) for _ in range(n+1)]
    for i in range(1,n+1):
        dis[i][i]=0  #자기 자신으로 가는것은 0 
        
    for i in range(m): #dis 행렬 초기화
        a ,b, c =map(int(input().split())) 
        dis[a][b]=c
    
    for k in range(1,n+1):  # k가 1부터 n+1 까지 계속돌면서 작은값으로 변경해주는것 
        for i in range(1,n+1):
            for j in range(1,n+1):
                dis[i][j] = min(dis[i][j], dis[i][k]+dis[k][j])
                
    for i in range(1,n+1):
        for j in range(1,n+1):
            if dis[i][j]==5000:
                print("M", end =' ')
            else:
                print(dis[i][j],end=' ')
        print()



    

