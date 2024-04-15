import sys
input = sys.stdin.readline

n , m  = map(int,input().split())

lst=[[0]*(m+2) for _ in range(n+2)]
for i in range(1,n+1):
    tmp = list(map(int,input().split()))
    lst[i][1:-1]=tmp



max_value=0
def fix_2(a,b):
    tmp=lst[a][b]+lst[a][b+1]
    k=max(lst[a-1][b-1]+lst[a-1][b],
        lst[a-1][b]+lst[a-1][b+1],
        lst[a+1][b-1]+lst[a+1][b],
        lst[a+1][b]+lst[a+1][b+1],
        lst[a-1][b+1]+lst[a+1][b],
        lst[a-1][b]+lst[a+1][b+1],
        )
    if b+2<m:
        t= max(lst[a+1][b+1]+lst[a+1][b+2],
            lst[a-1][b+1]+lst[a-1][b+2])
        k=max(k,t)
    return max(max_value,tmp+k)
        
    

def fix_3(a,b):
    tmp=lst[a][b-1]+lst[a][b]+lst[a][b+1]
    k=max(lst[a-1][b-1],lst[a-1][b],lst[a-1][b+1],
        lst[a+1][b-1],lst[a+1][b],lst[a+1][b+1],
        )
    if b+1<m:
        k=max(k,lst[a][b+2])
        
    tmp2 = lst[a][b]+lst[a-1][b]+lst[a+1][b]
    s=max(lst[a-1][b-1],lst[a][b-1],lst[a+1][b-1],
        lst[a+1][b+1],lst[a][b+1],lst[a-1][b+1]
        )
    if a+1<n:
        s=max(s,lst[a+2][b])
    return max(max_value,tmp+k,tmp2+s)
    
for i in range(1,n+1):
    for j in range(1,m+1):
        max_value= max(max_value,fix_2(i,j),fix_3(i,j))
        
print(max_value)
                  
                  