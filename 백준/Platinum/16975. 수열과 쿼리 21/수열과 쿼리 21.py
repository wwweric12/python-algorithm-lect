import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))
m = int(input())


tree=[0 for _ in range(n*4)]

lazy=[0 for _ in range(n*4)]



def init(start, end,index):

    if start >= end:
        tree[index] = lst[start]
        return tree[index]

    mid = (start+end)//2
    tree[index] = init(start,mid,index*2) + init(mid+1, end, index*2+1)

    return tree[index]






def update(start,end,left,right, value, index):
    if start>right or end< left : 
        return

    mid =(start+end)//2
    if left<= start and end <= right:
        lazy[index]+= value
        return


    tree[index] += (min(end,right)-max(start,left)+1)*value
        
    update(start,mid,left,right,value,index*2)
    update(mid+1,end,left,right,value,index*2+1)


def gangsin(left, right ,index):
    if lazy[index] != 0:
        tree[index]+= (right-left+1)*lazy[index]
        if left != right:
            lazy[index*2] +=  lazy[index]
            lazy[index*2+1] += lazy[index]
        lazy[index] = 0

    

def cal(start,end,value_index ,index):
    if start> value_index or end< value_index :
        return

    
    if lazy[index] != 0:
        gangsin(start, end, index)


    if start == value_index and end == value_index:
        print(tree[index])
        return


    mid =(start+end)//2
    cal(start,mid,value_index,index*2) 
    cal(mid+1,end,value_index,index*2+1) 

    


init(0,n-1,1)



for _ in range(m):
    tmp = list(map(int,input().split()))
    flag = tmp[0]    
   
    if flag == 1:
        update(0,n-1,tmp[1]-1,tmp[2]-1,tmp[3],1)
    else:
        cal(0,n-1,tmp[1]-1,1)
