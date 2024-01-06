# 가장 작은위치에 있는 말이 lt
# 가장 큰위치에 있는 말이  rt
# 그래서 중간값이 가장 최대로 거리일때 모든말들은 그것보다 커야되서 c가 가능한지 

n,c= map(int,input().split())


lst=[]
for i in range(n):
    lst.append(int(input()))

lst.sort()


lt=1

rt=lst[n-1]-1
answer=0
while lt<=rt:
    mid = (lt+rt)//2
    cnt=1
    tmp=lst[0]
    for i in lst:
        if i-tmp >=mid:
            cnt+=1
            tmp=i
    if cnt >= c:
        answer=mid
        lt = mid + 1 
    else:
        rt = mid - 1
        
print(answer)
            
            
            

# 답안


# def Count(len):
#     cnt=1
#     ep=Line[0]
#     for i in range(1,n-1):
#         if Line[i]-ep >= len:
#             cnt+=1
#             ep=Line[i]
        
#     return cnt


# n,c= map(int,input().split())




# Line=[]
# for _ in range(n):
#     Line.append(int(input()))

# Line.sort()


# lt=1
# rt=Line[len(Line)-1]
# res=0

# while lt<=rt:
#     mid = (lt+rt)//2
#     if Count(mid)>=c:
#         res =mid
#         lt=mid+1
#     else:
#         rt =mid-1
        
# print(res)