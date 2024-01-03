# n , m=map(int,input("n,m 입력").split())
# lst =[]
# for i in range(1,n+1):
#     for j in range(1, m+1):
#         lst.append(i+j)
        
# count =0     
# lst.sort()
# arr =[]
# for k in range(n+m):
#     if count < lst.count(k):
#         count = lst.count(k)
#         arr.clear()
#         arr.append(str(k))
#     elif count == lst.count(k):
#         arr.append(str(k))


# result =" ".join(arr)
# print(result)

n , m=map(int,input("n,m 입력").split())

cnt = [0]*(n+m+3)

for i in range(1,n+1):
    for j in range(1,m+1):
        cnt[i+j]+=1
tmp = 0
for k in range(len(cnt)):
    if tmp < cnt[k]:
        tmp =cnt[k]

for k in range(len(cnt)):
    if tmp == cnt[k]:
        print(k,end=' ')
    
