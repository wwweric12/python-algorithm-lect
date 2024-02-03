a = input()
b = input()

k = dict()

for i in a:
    if i in k.keys():
        k[i]+=1
    else:
        k[i]=1

for i in b:
    if i in k.keys():
        k[i]-=1
    else:
        print("NO")
        break
else:
    for key,val in k.items():
        if val!=0:
            print("NO")
            break
    else:
        print("YES")


#답안

a = input()
b = input()

str1 = dict()
str2 = dict()

for x in a:
    str1[x] = str1.get(x,0)+1 # 존재하는경우 +1 존재하지 않는경우 0으로 초기화 한다음에 +1

for x in b:
    str2[x]=str2.get(x,0)+1

for i in str1.keys():
    if i in str2.keys():
        if str1[i]!=str2[i]:
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")