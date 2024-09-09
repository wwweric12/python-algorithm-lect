import sys
sys.setrecursionlimit(10**8)
lst= list(map(int,input().split()))

ch=[[0 for _ in range(1503)] for _ in range(1503)]

def select(x,y):
    ch[x][y]=1
    ch[y][x]=1
    if x> y:
        x-=y
        y*=2
        return x,y
    else:
        y-=x
        x*=2
        return x,y


def same_number(a,b,c):
    if a==b==c:
        print(1)
        sys.exit()
    else:
        if b!=value and c!=value and b!=c and ch[b][c]==0:
            nb, nc=select(b,c)
            same_number(a,nb,nc)
        if a!=value and c!=value and a!=c and ch[a][c]==0:
            na, nc=select(a,c)
            same_number(na,b,nc)
        if a!= value and b!=value and a!=b and ch[a][b]==0:
            na, nb=select(a,b)
            same_number(na,nb,c)
        

if sum(lst)%3!=0:
    print(0)
    sys.exit()
else:
    value=sum(lst)//3
    same_number(lst[0],lst[1],lst[2])
    print(0)
    
    