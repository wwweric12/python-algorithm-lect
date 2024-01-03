#봉우리

# n=int(input("몇칸"))

# lst=[]
# count =0
# for _ in range(n):
#     tmp = list(map(int,input(str(n)+"개입력").split()))
#     tmp.insert(0,0)
#     tmp.append(0)
#     lst.append(tmp)
# lst.insert(0,[0]*(n+2))
# lst.append([0]*(n+2))

# print(lst)
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         tmp = lst[i][j]
#         if lst[i-1][j]<tmp and lst[i][j-1]<tmp and lst[i][j+1]<tmp  and lst[i+1][j]<tmp :
#             count +=1
            
            
            
# print(count)
        


#답안

n=int(input("몇칸"))

dx=[-1,0,1,0]
dy=[0,1,0,-1]

lst=[]
count =0
for _ in range(n):
    tmp = list(map(int,input(str(n)+"개입력").split()))
    tmp.insert(0,0)
    tmp.append(0)
    lst.append(tmp)
lst.insert(0,[0]*(n+2))
lst.append([0]*(n+2))

for i in range(1,n+1):
    for j in range(1,n+1):
        if all(lst[i][j]>lst[i+dx[k]][j+dy[k]] for k in range(4)): # all안에 모든조건이 참이면 참
            count+=1
        
