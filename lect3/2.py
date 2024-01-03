# import math
# s = input("입력")

# n =''
# answer =0
# for i in s:
#     if i in "0123456789":
#         n+=i
# n =int(n)
# print(n)

# for j in range(1,int(math.sqrt(n)+1)):
#     if n%j == 0:
#         answer+=2
# print(answer)

s = input("입력")

res =0
for i in s:
    if i.isdigit():
       res = 10*res+int(i)
print(res) 

cnt = 0
for j in range(1,res+1):
    if res%j ==0:
        cnt+=1
print(cnt)