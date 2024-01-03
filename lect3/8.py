# #곳감

# n = int(input("몇칸인가 홀수 만 가능 "))

# lst=[]
# for i in range(n):
#     lst.append(list(map(int,input(str(i+1)+"칸에 들어갈 숫자" +str(n)+"개").split())))
#     if max(lst[i])>100:
#         print("격자안에 사과의 개수가 100을 넘습니다 다시 시도해주세요")
#         break
    
# k= int(input("몇번 회전할래?"))

# for i in range(k):
#     lst1=list(map(int,input(str(i+1)+"번째").split()))
#     lst2=lst[lst1[0]-1]+lst[lst1[0]-1]
#     if lst1[1]==0:
#         lst[lst1[0]-1]=lst2[lst1[2]:lst1[2]+5]
#     else:
#         lst[lst1[0]-1]=lst2[5-lst1[2]:10-lst1[2]]
        
# answer=0
# s=0
# e=n
# for i in range(n):
#     for j in range(s,e):
#         answer+=lst[i][j]
#     if i < n//2:
#         s+=1
#         e-=1
#     else:
#         s-=1
#         e+=1

# print(answer)
    
    
# 답안 

n = int(input())

a=[list(map(int,input().split())) for _ in range(n)]
m=int(input())
for i in range(m):
    h, t, k =map(int,input().split())
    if t==0:
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0)) # pop(0)을 하면 가장 앞에꺼는 빠지고 하나씩 땡겨진다고 생각하면된다
    else:
        for _ in range(k):
            a[h-1].insert(0,a[h-1].pop())
    

res=0
s=0
e= n-1

for i in range(n):
    for j in range(s,e+1):
        res+=a[i][j]
    if i< n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1
print(res)