n = int(input())
chess=[0 for _ in range(n)]

cnt=0

def QueenLocation_DFS(L):
    global cnt
    if L==n:
        cnt+=1
        return 
    
    else:
        for i in range(n):
            chess[L]=i
            if check_location(L):
                QueenLocation_DFS(L+1)
                

def check_location(x):
    for i in range(x):
        if chess[x]==chess[i] or abs(chess[i]-chess[x])== abs(x-i):
            return False
    return True
    
            
QueenLocation_DFS(0)
print(cnt)


