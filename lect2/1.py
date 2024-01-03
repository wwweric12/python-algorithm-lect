def solution(n,k):
    lst = []
    for i in range(1,n+1):
        if(n%i==0):
            lst.append(i)
    if len(lst) <k:
        answer = -1
    else:
        answer = lst[k-1]
    return answer
    

print(solution(6,3))

# cnt=0
# for i in range(1, n+1):
#     if n%i==0:
#         cnt+=1
#     if cnt==k:
#         print(i)
#         break
# else:
#     print(-1)