n = int(input())
num_lst = list(map(int,input().split()))
calculate_lst =list(map(int,input().split()))


max_value=-1000000000
min_value=1000000000

def DFS(L,sum_value):
    global min_value,max_value
    if L ==n-1:
        min_value=min(min_value,sum_value)
        max_value=max(max_value,sum_value)
        return
    else:
        for i in range(4):
            if calculate_lst[i]!=0:
                calculate_lst[i]-=1
                if i ==0:
                    result_value=sum_value+num_lst[L+1]
                elif i== 1:
                    result_value=sum_value-num_lst[L+1]
                elif i == 2:
                    result_value=sum_value*num_lst[L+1]
                else:
                    if sum_value<0:
                        result_value=-1*((-1*sum_value)//num_lst[L+1])
                    else:
                        result_value=sum_value//num_lst[L+1]
                DFS(L+1,result_value)
                calculate_lst[i]+=1
                
DFS(0,num_lst[0])             
print(max_value)
print(min_value)