n = int(input())

lst=[]
for x in range(2*n-1):
    k=input()
    if k in lst:
        lst.remove(k)
    else:
        lst.append(k)

print(lst[0])

#답안

# n = int(input())
# p = dict()
# for i in range(n):
#     word = input()
#     p[word]=1

# for i in range(n-1):
#     word = input()
#     p[word]=0
    
# for key,val in p.items():
#     if val ==1 :
#         print(key)
#         break

