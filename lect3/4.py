a = int(input(""))
lst1 = list(map(int,input("").split()))

b = int(input(""))
lst2 = list(map(int,input("").split()))

# lst=lst1+lst2
# lst.sort()

# for i in lst:
#     print(i,end=" ")

lst =[]
n = 0 
k = 0
while 1:
    if(lst1[n]<=lst2[k] ):
        lst.append(lst1[n])
        n+=1
    else:
        lst.append(lst2[k])
        k+=1
    if a==n :
        lst += lst2[k:]
        break
    if b==k :
        lst += lst1[k:]
        break

for i in lst:
    print(i,end=" ")
        