import sys
input = sys.stdin.readline

n = int(input())
lst=[]
for i in range(n):
    tmp=list(map(int,input().split()))
    lst.append(tmp)
    
min_value= 10000
ch=[0]*n

def DFS(L):
    global min_value    
    if L == n:
        left=[]
        right=[]
        left_value=0
        right_value=0
        for i in range(n):
            if ch[i]==1:
                left.append(i)
            else:
                right.append(i)
        if len(left) >1 and len(right) >1 :
            for j in range(len(left)):
                for k in range(j,len(left)):
                    if k !=j:
                        left_value+=lst[left[j]][left[k]]+lst[left[k]][left[j]]

            for j in range(len(right)):
                for k in range(j,len(right)):
                    if k !=j:
                        right_value+=lst[right[j]][right[k]]+lst[right[k]][right[j]]
                        
            if min_value > abs(left_value-right_value):
                min_value=abs(left_value-right_value)
                if min_value == 0:
                    print(0)
                    sys.exit()
        return 
    else:
        ch[L]=1
        DFS(L+1)
        ch[L]=0     
        DFS(L+1)           


DFS(0)


print(min_value)