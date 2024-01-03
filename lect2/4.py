n=int(input("몇명의 사람"))
lst=list(map(int,input("점수"+str(n)+"개입력").split()))
arr=[]
total=0
for i in range(len(lst)): #sum(lst)방법있음 list의 합 
    total+=lst[i]
avg =total/n
avg =round(avg) #평균구하기 round 는 round_half_even방식이라  4.5 에 round 하면 4가된다 짝수쪽으로 가게 된다 
# a =66.5  a= a+0.5  a= int(a)이런식으로 반올림하자

tmp =100
for i in lst:    
    arr.append(abs(i-avg))
    if tmp > abs(i-avg):
        tmp= abs(i-avg)
        
arr=list(enumerate(arr,start=1))    

k=[]
cnt =0
for j in range(len(arr)):
    if arr[j][1]==tmp and lst[arr[j][0]-1]>avg :
        print(arr[j][0])
        cnt+=1
        break
    elif arr[j][1]==tmp:
        k.append(arr[j][0])

if cnt == 0 :
    print(k[0])


        










# for idx,x in enumerate(lst):  idx는 인덱스 값 x는 그인덱스의 값 



n=int(input("몇명의 사람"))
lst=list(map(int,input("점수"+str(n)+"개입력").split()))

avg = sum(lst)/n
avg = int(avg+0.5) #평균구하고 반올림하기 

t = lst[0]

for idx ,x in enumerate(lst):
    tmp =abs(x-avg)
    if t>tmp:
        t= tmp
        score = x
        answer = idx+1
    elif t == tmp:
         if score < x :
             score = x
             answer = idx+1 
print(avg,answer)