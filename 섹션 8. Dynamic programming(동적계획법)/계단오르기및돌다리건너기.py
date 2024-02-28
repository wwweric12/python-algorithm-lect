#계단오르기 
n= int(input())


dx = [0]*(n+1)
dx[1]=1
dx[2]=2

for i in range(3,n+1):
    dx[i]=dx[i-1]+dx[i-2]
print(dx[n])

# 돌다리건너기 

def DFS(len):
    if dy[len] !=0:
        return dy[len]
    if len == 1 or len ==2:
        return len
    else:
        dy[len]=DFS(len-1)+DFS(len-2)
        return dy[len]



if __name__ == "__main__":
    n= int(input())
    dy = [0]*(n+2)
    dy[1]=1
    dy[2]=2
    print(DFS(n+1))

