import sys
input = sys.stdin.readline
n= int(input())
lst=[]
for _ in range(n):
    k=[]
    tmp=input().strip()
    for i in tmp:
       k.append(i)
    lst.append(k) 

def row(i,j):
    cnt=0
    t=j
    while j>0 and lst[i][j] == lst[i][j-1] :
        cnt+=1
        j-=1
    while t<n-1 and lst[i][t] == lst[i][t+1] :
        cnt+=1
        t+=1
        
    return cnt+1 

def column(i,j):
    cnt=0
    t=i
    while i>0 and lst[i][j] == lst[i-1][j] :
        cnt+=1
        i-=1
    while t<n-1 and lst[t][j] == lst[t+1][j]:
        cnt+=1
        t+=1
    return cnt +1
res =0    
for i in range(n):
    for j in range(n):
        tmp1=column(i,j)
        tmp2=row(i,j)
        res= max(res,tmp1,tmp2)

if res ==n:
    print(n)
    sys.exit()
          
    

for i in range(n):
    for j in range(n):
        if j<n-1:
            if lst[i][j] != lst[i][j+1]:
                lst[i][j], lst[i][j+1] =lst[i][j+1], lst[i][j]
                tmp1=row(i,j)
                tmp2=column(i,j)
                tmp3=row(i,j+1)
                tmp4=column(i,j+1)
                res=max(tmp1,tmp2,res,tmp3,tmp4)
                lst[i][j], lst[i][j+1] =lst[i][j+1], lst[i][j]
        if i<n-1:
            if lst[i][j] != lst[i+1][j]:
                lst[i+1][j], lst[i][j] =lst[i][j], lst[i+1][j]
                tmp1=row(i,j)
                tmp2=column(i,j)
                tmp3=row(i+1,j)
                tmp4=column(i+1,j)
                res=max(tmp1,tmp2,res,tmp3,tmp4)
                lst[i+1][j], lst[i][j] =lst[i][j], lst[i+1][j]
        
print(res)