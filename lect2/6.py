n= input("몇개의 자연수")
lst=list(map(int,input(n+"개의 자연수 입력").split()))


# def digit_sum(x):
#     tmp=0
#     for j in str(x):
#         tmp+=int(j)
#     return tmp

def digit_sum(x):
    sum=0
    while x>0:
        sum+=x%10
        x//=10
    return sum


max= 0
for i in range(len(lst)):
    tmp = digit_sum(lst[i])
    if tmp>max:
        max =tmp
        answer =lst[i]
print(answer)
    


