# n = int(input("몇문제"))
# lst =list(map(int,(input("입력 맞고 틀리고").split())))

# score =0
# cnt =0
# for i in range(n-1):
#     if lst[i]== 1 :
#         score +=1
#         cnt+=1
#         if lst[i-1] == 1:
#             score +=cnt-1
#     else :
#         cnt=0
       
    
# print(score)


n = int(input("몇문제"))
lst =list(map(int,(input("입력 맞고 틀리고").split())))

sum=  0
cnt = 0
for i in lst:
    if i == 1:
        cnt+=1
        sum+=cnt
    else:
        cnt=0   
        
print(sum)