n=int(input())

lst =[list(map(int,input().split())) for _ in range(n)] 
lst.sort(key= lambda x:x[2],reverse=True)
dy=[0]*n
dy[0]=lst[0][1]
res=0

for i in range(1,n):
    tmp=0
    for j in range(i-1,-1,-1):
        if lst[i][0] < lst[j][0] and dy[j] > tmp:
            tmp = dy[j]
    dy[i] = tmp + lst[i][1]

print(max(dy))

#답안 

if __name__ == "__main__":
    n= int(input())
    bricks=[]
    for i in range(n):
        a , b, c = map(int,input().split())
        bricks.append((a,b,c))
    bricks.sort(reverse=True)
    dy=[0]*n
    dy[0]= bricks[0][1]
    for i in range(1,n):
        max_h=0
        for j in range(i-1,-1,-1):
            if bricks[j][2] > bricks[i][2] and dy[j] > max_h:
                max_h=dy[j]
        dy[i] = max_h + bricks[i][1]
        res=max(res,dy[i])
    print(res)
