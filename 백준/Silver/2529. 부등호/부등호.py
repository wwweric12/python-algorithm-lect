import sys
input = sys.stdin.readline
k = int(input())
lst=list(input().split())

ch_min=[0]*10
ch_max=[0]*10

min_state=True
max_state=True

min_tmp=[]
max_tmp=[]
min_res=[]
max_res=[]

def DFS(L):
    global min_state,max_state,min_res,max_res
    if min_state==False and max_state==False:
        for i in max_res:
            print(i,end='')
        print()
        for j in min_res:
            print(j,end='')
        print()
        sys.exit()
    if L == k+1:
        min_cnt=0
        max_cnt=0
        while min_state:
            if min_cnt ==k: 
                min_state= False
                min_res=min_tmp.copy()
                break
            if lst[min_cnt]== ">" and min_tmp[min_cnt] < min_tmp[min_cnt+1]:
                break
            elif lst[min_cnt] == "<" and min_tmp[min_cnt] > min_tmp[min_cnt+1]:
                break
            else:
                min_cnt+=1
                
        while max_state:
            if max_cnt ==k: 
                max_state= False
                max_res=max_tmp.copy()
                break
            if lst[max_cnt]== ">" and max_tmp[max_cnt] < max_tmp[max_cnt+1]:
                break
            elif lst[max_cnt] == "<" and max_tmp[max_cnt] > max_tmp[max_cnt+1]:
                break
            else:
                max_cnt+=1        
        return 
            
       
    else:
        for i in range(10):
            if ch_min[i]==0:
                ch_min[i]=1
                ch_max[9-i]=1
                min_tmp.append(i)
                max_tmp.append(9-i)
                DFS(L+1)
                min_tmp.pop()
                max_tmp.pop()
                ch_max[9-i]=0
                ch_min[i]=0
     
        
    
DFS(0)


    