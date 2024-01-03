
# n , k= map(int,input("몇장의카드(n)과 몇번째(k)의 수를 가질거니?").split()) 
# a = list(map(int,input("숫자입력").split()))
# lst=[]
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         for l in range(j+1,len(a)):
#             lst.append(a[i]+a[j]+a[l])
# answer =list(set(lst))
# answer.sort(reverse=True)
# print(answer[k-1])



# combination 써서 활용 (13, 15, 34), (13, 15, 23) 이런식으로 나옴 
import itertools

n , k= map(int,input("몇장의카드(n)과 몇번째(k)의 수를 가질거니?").split()) 
a = list(map(int,input("숫자입력").split()))
lst=[]
for i in itertools.combinations(a,3):
    lst.append(i[0]+i[1]+i[2])
answer =list(set(lst))
answer.sort(reverse=True)
print(answer[k-1])
