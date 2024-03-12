n= int(input())

lst=list(map(int,input().split()))
res=0

for i in lst:
    if i == 1 :
        continue
    elif i == 2:
        res+=1
        continue
    elif i %2 ==0:
        continue
    else:
        for j in range(3,i//2+1):
            if i%j == 0:
                break
        else:
            res+=1
        
print(res)