n,m = map(int,input("").split())
lst= list(map(int,input().split()))

lst.sort()
answer=0
for i in range(len(lst)):
    if(lst[i]==m):
        answer=i+1
        break
print(answer)

## 답안 

#lt, rt를 정해서 lt는 배열의 시작 지점(0번인덱스)  rt는 마지막 지점

#mid=(lt+ rt)//2 를 해서 구하고싶은값이 mid 보다 작은지 큰지 비교

#mid 보다작으면  lt ~ mid 사이 크면 mid 부터~ rt 

#ex)구하고 싶은 값의 index가 mid보다 작을때 rt = mid -1 로 해서 구함

#ex)구하고 싶은 값의 index가 mid보다  클때  lt = mid +1 로 해서 구함 

#계속 반복 하다보면 답이 구해짐 계속 절반씩 없어지고 결국 답을 구할 수 있음


import sys
sys.stdin=open("input.txt","r")
n, m = map(int,input().split())
a= list(map(int,input().split())) 
a. sort()

lt=0
rt= n-1

while lt<=rt:  # lt가 rt보다 커져버리면 탐색을 종료 
    mid= (lt+rt)//2
    if a[mid] ==m:
        print(mid+1)
        break
    elif a[mid] > m:
        rt = mid -1
    else: 
        lt = mid+1
    