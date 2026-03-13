import sys
input = sys.stdin.readline

n, m, k = map(int,input().split())

lst=[]

for i in range(n):
   lst.append(int(input()))


tree=[0 for _ in range(n*4)]
lazy=[0 for _ in range(n*4)]

def init(left, right,index):
    mid = (left+right)//2
    if left>= right:
        tree[index] = lst[mid]
        return tree[index]
    tree[index] = init(left,mid,index*2)+ init(mid+1,right,index*2+1)
    return tree[index]

init(0,n-1,1)


def lazy_propa(start,end,index):
    if lazy[index] != 0:
        tree[index]+= (end-start+1)*lazy[index]
    
        if start != end:
            lazy[index*2] += lazy[index]
            lazy[index*2+1] += lazy[index]
        lazy[index]=0


def update(left,right, start,end, value, index):
    lazy_propa(left,right,index)
    if start> right or end < left:
        return

    
    if start <= left and right <= end:
        lazy[index]+= value
        lazy_propa(left,right,index)
        return 



    
    mid= (left+right)//2 
    update(left,mid,start,end,value,index*2)
    update(mid+1,right,start,end,value,index*2+1) 

    tree[index] = tree[index*2] + tree[index*2+1]


def cal(left,right,start,end,index):
    lazy_propa(left,right,index)
    if start > right or end < left :
        return 0

    mid = (left+right)//2

    if start <= left and right <= end:
        return tree[index]

    return cal(left,mid,start,end,index*2)+cal(mid+1,right,start,end,index*2+1)
        




for i in range(m+k):
    tmp = list(map(int,input().split()))
    if tmp[0] == 1:
        update(0,n-1,tmp[1]-1,tmp[2]-1,tmp[3],1)
       
       


    else:
        res= cal(0,n-1,tmp[1]-1,tmp[2]-1,1)
        print(res)