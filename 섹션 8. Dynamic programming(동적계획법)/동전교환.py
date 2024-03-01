n= int(input())
lst=list(map(int,input().split()))
s = int(input())

dy=[k for k in range(s+1)]
for i in range(n):
    for j in range(lst[i],s+1):
        dy[j] = min(dy[j],dy[j-lst[i]]+1)


print(dy[s])
        
#답안

if __name__ == "__main__":
    n= int(input())
    coin=list(map(int,input().split()))
    m = int(input())
    dy=[1000]*(m+1)
    dy[0]=0
    for i in range(n):
        for j in range(coin[i],m+1):
            dy[j] = min(dy[j],dy[j-coin[i]]+1)
    print(dy[m])

