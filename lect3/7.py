# 사과나무 

# n = int(input("몇칸인가 홀수 만 가능 "))

# lst=[]
# for i in range(n):
#     lst.append(list(map(int,input(str(i+1)+"칸에 들어갈 숫자" +str(n)+"개").split())))
#     if max(lst[i])>100:
#         print("격자안에 사과의 개수가 100을 넘습니다 다시 시도해주세요")
#         break

# cnt =0
# answer=0
# dup=0
# while(n!=cnt):
#     for i in range(n//2+1-dup-1,n//2+1+dup):
#         answer+= lst[cnt][i]
#     cnt+=1
#     if cnt<n//2+1:
#         dup+=1
#     else:
#         dup-=1
    
        
# print(answer)
    
    
    
# 답안

n= int(input())

a= [list(map(int,input().split())) for _ in range(n)]
res =0

s= e =n//2

for i in range(n):
    for j in range(s,e+1):
        res+=a[i][j]
    if i<n//2:
        s-=1
        e+=1
    else:
        s+=1
        e-=1
    
print(res)
