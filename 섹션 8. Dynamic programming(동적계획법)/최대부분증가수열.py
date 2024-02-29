n = int(input())
lst = list(map(int,input().split()))


dy=[0]*n
dy[0]=1

for i in range(1,n):
    tmp=0
    for j in range(i-1,-1,-1):
        if lst[i]> lst[j] and tmp < dy[j]:
            tmp = dy[j]
    dy[i]=tmp+1

        
print(max(dy))







#답안 

# n = int(input())
# arr=list(map(int,input().split()))

# arr.insert(0,0)
# dy = [0]*(n+1)
# dy[1]=1
# res=0

# for i in range(2,n+1):
#     max =0
#     for j in range(i-1,0,-1):
#         if arr[j] < arr[i] and dy[j] >max:
#             max= dy[j]
#     dy[i]=max +1
#     if dy[i] >res :
#         res= dy[i]
            
# print(res)






