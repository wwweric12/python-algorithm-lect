# n이 50보다 작음 

n = int(input())

plus=[]
minus=[] 
zero=0
res=0

for _ in range(n):
    tmp = int(input())
    if tmp == 1:
        res+=1
        
    elif tmp>0:
        plus.append(tmp)
    elif tmp ==0:
        zero+=1
    else:
        minus.append(tmp)
    



## 1. 일단 큰것들의 곱으로 묶는거 첫번째
## 2. 마이너스들 끼리도 묶어야함 
## 3. 0은 마이너스와의 곱이 좋음 
## 4. 1은 무조건 더하기

plus.sort(reverse=True)
minus.sort()


len_plus = len(plus)
len_minus = len(minus)

if len_plus > 1:
    if len_plus%2 == 0:
        for i in range(1,len_plus,2):
            res+= plus[i]*plus[i-1]
        
    else:
        for i in range(1,len_plus-1,2):
            res+= plus[i]*plus[i-1]
        res+=plus[-1]
elif len_plus == 1:
    res += plus[0]
    
    
if len_minus > 1:
    if len_minus%2 ==0:
        for i in range(1,len_minus,2):
            res+= minus[i]*minus[i-1]
    else:
        for i in range(1,len_minus,2):
            res+= minus[i]*minus[i-1]

        
        if zero==0:
            res +=minus[-1]

elif len_minus == 1:
    if zero == 0:
        res += minus[0]
    

print(res)
