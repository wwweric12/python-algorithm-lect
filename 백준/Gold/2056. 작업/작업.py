from collections import deque

n = int(input())

lst=[[]for _ in range(n+1)]
res=0
Q= deque()
ch=[0 for _ in range(n+1)] # 선행관계 
time =[0 for _ in range(n+1)] # 총 걸리는 시간 
res=[0 for _ in range(n+1)]
for i in range(1,n+1):
    tmp =list(map(int,input().split()))
    time[i]=tmp[0]
    ch[i]=tmp[1]
    if tmp[1]!=0:
        for j in tmp[2:]:
            lst[j].append(i)
for i in range(1,n+1):
    if ch[i]==0:
        Q.append([time[i],i])
    


while Q:
    end, index = Q.popleft()  ## 영향 미치는 곳 , 이걸 진행했을 때 끝난 초 
    for i in lst[index]:
        ch[i]-=1
        res[i] = max(res[i],end) ## i가 끝났을 때 최대 진행 초 
        if ch[i]==0:
            tmp = res[i]+time[i]
            Q.append([tmp,i])
    if lst[index]==[]:
        res[index]=end
        
print(max(res))

        
    
            
