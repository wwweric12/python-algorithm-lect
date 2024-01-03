# n= int(input("몇명?"))


# answer =0
# for i in range(n):
#     m = 0
#     lst=list(map(int,input("3개의 주사위 입력").split()))
#     if len(set(lst))== 1:
#         m = 10000+max(lst)*1000
#     elif len(set(lst))== 2:
#         if lst[0] ==lst[1] or lst[0] == lst[2]:
#             m = 1000+lst[0]*100
#         else :
#             m = 1000+lst[1]*100
#     else :
#         m = max(lst)*100
#     if m > answer:
#         answer =m 
        
    

# print(answer)


n= int(input("몇명?"))


answer =0
for i in range(n):
    tmp = input("3개 주사위 입력").split()
    a, b, c = map(int,tmp)
    if a == b and b ==c:
        money = 10000+a*1000
    elif a==b or a==c:
        money = 1000+a*100
    elif b==c:
        money = 1000+b*100
    else:
        money = max(a,b,c)*100
    if money > answer:
        answer=money
print(answer)