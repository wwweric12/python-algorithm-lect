n = int(input())
lst=[]
for i in range(n):
    tmp=list(map(int,input().split()))
    lst.append(tmp)
    
min_value= 100
ch=[0]*n

def DFS(L,S):
    global min_value
    if L == n/2:
        left=[]
        right=[]
        left_value=0
        right_value=0
        for i in range(n):
            if ch[i]==1:
                left.append(i)
            else:
                right.append(i)
        for j in range(L):
            for k in range(j,L):
                if k !=j:
                    left_value+=lst[left[j]][left[k]]+lst[left[k]][left[j]]
                    right_value+=lst[right[j]][right[k]]+lst[right[k]][right[j]]
        if min_value > abs(left_value-right_value):
            min_value=abs(left_value-right_value)
        return 
        
                
    else:
        for i in range(S,n):
            if ch[i]==0:
                ch[i]=1
                DFS(L+1,i)
                ch[i]=0


DFS(0,1)
print(min_value)


