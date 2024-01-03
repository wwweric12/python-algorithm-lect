k,n=map(int,input().split())


lst=[]
for i in range(k):
    lst.append(int(input()))
lt=1
rt = max(lst)


answer=0
while lt<=rt:
    tmp=0 
    mid = (lt+rt)//2
    for i in range(len(lst)):
        tmp+=lst[i]//mid
    if tmp>=n:
        lt=mid+1
        answer=mid
    else:
        rt=mid-1


    
print(answer)
 
    
    
# 답안

# 이분탐색은 결정알고리즘에서 사용한다
# 값이 범위안에 있을때 사용 

import sys
sys.stdin = open("input.txt","r")

def Count(len):
    cnt=0
    for x in Line:
        cnt+=(x//len)
    return cnt


k,n=map(int,input().split())
Line=[]
res =0


largest=0
for i in range(k):
    tmp=int(input())
    Line.append(tmp)
    largest=max(largest,tmp)
lt=1
rt=largest

while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=n:
        res=mid
        lt=mid+1
    else:
        rt=mid-1

print(res)
        
