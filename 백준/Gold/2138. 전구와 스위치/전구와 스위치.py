import copy
n= int(input())

a_lst=list(map(int,input().strip()))
b_lst=list(map(int,input().strip()))



def change(num,lst):
    if num ==0 :
        lst[num] =(lst[num]+1)%2
        lst[num+1] =(lst[num+1]+1)%2
    elif num ==n-1:
        lst[num] =(lst[num]+1)%2
        lst[num-1] =(lst[num-1]+1)%2
    else:
        lst[num] =(lst[num]+1)%2
        lst[num-1] =(lst[num-1]+1)%2
        lst[num+1] =(lst[num+1]+1)%2


cp_lst=copy.deepcopy(a_lst)
a_cnt=1
cp_cnt=0
change(0,a_lst)        

for i in range(1,n):
    if a_lst[i-1]!=b_lst[i-1]:
        change(i,a_lst)
        a_cnt+=1
        
for i in range(1,n):
    if cp_lst[i-1]!=b_lst[i-1]:
        change(i,cp_lst)
        cp_cnt+=1
        
a_state=True
cp_state=True

for i in range(n):
    if a_state :
        if a_lst[i]!=b_lst[i]:
            a_state=False
    if cp_state:
        if cp_lst[i]!=b_lst[i]:
            cp_state=False
            
            
if a_state and cp_state:
    print(min(a_cnt,cp_cnt))
elif a_state:
    print(a_cnt)
elif cp_state:
    print(cp_cnt) 
else:
    print(-1)
    






