n=int(input())
lst=[]
for _ in range(n):
    lst.append(list(map(int,input().split())))

lst.sort(key= lambda x : x[1])

tmp =lst[0][1]
cnt =1

for i in lst:
    if i[0]>=tmp:
        cnt+=1
        tmp = i[1]
print(cnt)


    
# 답안

# n = int(input())

# meeting=[]
# for i in range(n):
#     s,e = map(int,input().split())
#     meeting.append((s,e)) 
# # 튜플을 사용하는이유로는 메모리 효율성, 데이터 안정성, 관리의 편리성    
# meeting.sort(key=lambda x : (x[1],x[0])) # 뒤에꺼가 정렬기준이 되는거임
# et= 0
# cnt =0

# for s, e in meeting:
#     if s>= et:
#         et=e
#         cnt+=1

# print(cnt)


