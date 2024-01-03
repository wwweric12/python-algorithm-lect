#격자판 최대합

n = int(input())

lst=[]
for _ in range(n):
    lst.append(list(map(int,input().split())))

max_num=0

#가로 합 중 가장 큰 수 뺴오기 
for i in lst:
    if max_num < sum(i):
        max_num= sum(i)
        
        
sum_index =0


# 세로 합중 가장 큰수 빼오기 
for i in range(len(lst)):
    for j in range(len(lst[i])):
        sum_index +=lst[j][i]
    if max_num <sum_index :
        max_num = sum_index
    sum_index =0




# 대각선
for i in range(len(lst)):
    sum_index +=lst[i][i]
if max_num <sum_index :
    max_num = sum_index
    

sum_index = 0

for i in range(len(lst)-1,-1,-1):
    sum_index +=lst[i][i]
if max_num <sum_index :
    max_num = sum_index
    
print(max_num)

    

    

