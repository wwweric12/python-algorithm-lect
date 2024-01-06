n,m= map(int,input().split())
lst=list(map(int,input().split()))

lt=1
rt=sum(lst)
maxx=max(lst)


answer=0

while lt<=rt:
    mid= (lt+rt)//2
    cnt=1
    tmp=0
    for i in lst:
        tmp+=i
        if tmp >mid :
            cnt+=1
            tmp=i 
    if mid >=maxx and  cnt <= m:
        rt=mid-1
        answer=mid
    else:
        lt=mid+1
        
        
print(answer)
        

    
    











# 답안


# def Count(capacity):
#     cnt=1
#     sum=0
#     for x in lst:
#         if sum+x>capacity:
#             cnt+=1
#             sum=x
#         else:
#             sum+=x
#     return cnt


# n,m= map(int,input().split())
# lst=list(map(int,input().split()))

# lt=1
# rt=sum(lst)
# res =0
# maxx = max(lst)

# while lt<=rt:
#     mid = (lt+rt)//2
#     if mid >=maxx and Count(mid)<=m:
#         res = mid
#         rt=mid-1
#     else:
#         lt = mid+1

# print(res)