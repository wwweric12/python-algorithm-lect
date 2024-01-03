# n=int(input("입력 n까지의 소수의 개수"))
# lst=[]
# for i in range(2,n+1):
#     lst.append(i)
# t=0
# while t<len(lst):
#     prime =lst[t]
#     j =t+1
#     while j <len(lst):
#         if lst[j]%prime==0:
#             lst.pop(j)
#         else: 
#             j+=1
#     t+=1   
        
# print(len(lst))

n=int(input("입력 n까지의 소수의 개수"))

lst=[0]*(n+1)
cnt=0
for i in range(2,n+1):
    if lst[i]==0:
        cnt+=1    
        for j in range(i,n+1,i):
            lst[j]=1
print(cnt)
