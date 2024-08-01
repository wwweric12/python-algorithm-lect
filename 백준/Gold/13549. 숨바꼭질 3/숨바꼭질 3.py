from collections import deque

n,k =map(int,input().split())
Q=deque()
Q.append(n)
ch=[-1]*100001
ch[n]=0
while True:
    tmp=Q.popleft()
    if tmp == k:
        print(ch[k])
        break
    for i in (2*tmp,tmp-1,tmp+1):
        if 0<=i <=100000 and ch[i] ==-1 :
            if i == 2*tmp :
                ch[i]=ch[tmp]
                Q.appendleft(i)
            else:
                ch[i]=ch[tmp]+1
                Q.append(i)
            
            
  


    