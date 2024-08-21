n= int(input())
numbers= list(map(int,input().split()))
calculate= list(map(int,input().split()))


max_value=-1000000000
min_value=1000000000

def DFS(L,value):
    global max_value,min_value
    if L==n:
        max_value=max(max_value,value)
        min_value=min(min_value,value)
        
    else:
        for i in range(4):
            if calculate[i]!=0:
                calculate[i]-=1
                if i== 0: 
                    DFS(L+1,value+numbers[L])
                elif i== 1: 
                    DFS(L+1,value-numbers[L])
                elif i== 2: 
                    DFS(L+1,value*numbers[L])
                elif i== 3: 
                    if value<0:
                        DFS(L+1,-1*(abs(value)//numbers[L]))
                    else:
                        DFS(L+1,value//numbers[L])
                calculate[i]+=1
                
DFS(1,numbers[0])
print(max_value)              
print(min_value)
        
    
    

