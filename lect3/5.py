# 수들의 합 

# n,k =map(int,input("몇개의 수 와 합쳤을때 값").split())
# lst= list(map(int,input("수 입력").split()))

# tmp= 0
# cnt =0

# i=0
# j=0

# while j <=n-1:
    
#     tmp+=lst[i]
#     if k ==tmp:
#         cnt+=1
#         tmp=0
#         j+=1
#         i=j   
#     elif tmp > k:
#         tmp =0
#         j+=1
#         i=j
#     elif i==len(lst)-1 and tmp< k:
#         tmp =0
#         j+=1
#         i=j
#     else :
#         i+=1
        
    

# print(cnt)
    
    
n,k =map(int,input("몇개의 수 와 합쳤을때 값").split())
lst= list(map(int,input("수 입력").split()))

tot=lst[0]
cnt=0
lt=0
rt=1

while True:
    if tot<k:
        if rt<n:
            tot+=lst[rt]
            rt+=1
        else:
            break 
    elif tot == k:
        cnt+=1
        tot-=lst[lt]
        lt+=1
    else:
        tot-=lst[lt]
        lt+=1
        
print(cnt)