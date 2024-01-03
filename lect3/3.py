# lst=[]
# for i in range(1,21):
#     lst.append(i)

# for j in range(10):
#     a, b = map(int,input("입력").split())
#     tmp = lst[a-1:b]
#     lst[a-1:b]=tmp[::-1]  
  
# for j in lst:
    # print(j, end=" ")

lst =list(range(1,21))


for _ in range(10):
    a , b = map (int,input("입력").split())
    for i in range((b-a+1)//2):
        lst[a-1+i],lst[b-1-i] = lst[b-1-i] ,lst[a-1+i]

for j in lst:
    print(j, end=" ")
    