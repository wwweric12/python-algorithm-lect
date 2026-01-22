import sys

input = sys.stdin.readline
tree=[]
lst=[]


def cal(value):
    if value <0 :
        return -1
    elif value > 0:
        return 1
    else:
        return 0


def init(start,end,index):
    if start == end:
        tree[index]= cal(lst[start])
        return tree[index]
    
    mid = (start+end)//2
    tree[index] = init(start,mid,index*2)*init(mid+1,end,index*2+1)
    return tree[index]

def update(start,end,index,next,target):
    if target< start or target>end:
        return tree[index]
    
    if start == end:
        tree[index] =cal(next)
        return tree[index]

    mid = (start + end) // 2
    tree[index] = update(start, mid, index * 2, next,target ) * update(mid + 1, end, index * 2 + 1, next, target)
    return tree[index]
    

def check(start,end,index,i,j):
    if i<=start and j>= end:
        return tree[index]
    
    if i > end or j < start:
        return 1 
    
    mid = (start+end)//2
    return check(start,mid,index*2,i,j)*check(mid+1,end,index*2+1,i,j)
    
    
    
    

    

while True:
    res=""
    line = input()
    if not line:
        break
    n, k = map(int, line.split())
    lst = list(map(int, input().split()))
    tree = [0 for _ in range(4*n)]
    
    init(0,n-1,1)

    
    for _ in range(k):
        command, i, j = input().split()
        i= int(i)
        j= int(j)
        if command == "C":
            update(0,n-1,1,j,i-1)
        else:
            tmp = check(0,n-1,1,i-1,j-1)
            
            if tmp == 0:
                res+="0"
            elif tmp<0:
                res+="-"
            else:
                res+="+"
    print(res)