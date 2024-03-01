n , m = map(int,input().split())
lst=[list(map(int,input().split())) for _ in range(n)]

dy=[0]*(m+1)
ch=[[] for _ in range(m+1)]

for i in range(n):
    tch=ch.copy()
    tdy =dy.copy()
    for j in range(lst[i][1],m+1):
        if dy[j] < dy[j-lst[i][1]]+lst[i][0] and (i not in tch[j-lst[i][1]]):
            ch[j]=tch[j-lst[i][1]] + [i]
            dy[j] =tdy[j-lst[i][1]]+lst[i][0]
    
    
print(dy[m])

#답안

if __name__ == "__main__":
    n , m = map(int,input().split())
    dy=[0]*(m+1)
    for i in range(n):
        ps, pt = map(int,input().split())
        for j in range(m,pt-1,-1):
            dy[j]= max(dy[j],dy[j-pt]+ps)
    print(max(dy))



