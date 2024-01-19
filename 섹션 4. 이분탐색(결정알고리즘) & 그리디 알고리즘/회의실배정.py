n=int(input())
lst=[]
for _ in range(n):
    lst.append(list(map(int,input().split())))

lst.sort(key= lambda x : (x[1],x[0]))

tmp =lst[0][1] 
cnt =1
for i in range(1,len(lst)):
    if lst[i][0]>=tmp:
        cnt+=1
        tmp = lst[i][1]
print(cnt)

# 하나만 있는 회의인경우 일때
# ex)3,3 일때 for문이 돌기때문에 cnt가 1 증가해서 틀림 



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


