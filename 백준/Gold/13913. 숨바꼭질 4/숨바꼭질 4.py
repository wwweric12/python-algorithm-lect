from collections import deque

n,k = map(int,input().split())
Q=deque()

ch=[[-1,-1] for _ in range(100001)]
ch[n][0]=0
Q.append(n)
res=[]


while True:
    tmp = Q.popleft()
    if tmp ==k:
        print(ch[k][0])
        back=k
        res.append(k)
        while back!=n:
            res.append(ch[back][1])
            back=ch[back][1]         
        for a in res[::-1]:
            print(a,end=' ')
        break
    else:
        for i in (tmp-1,tmp+1,2*tmp):
            if 0<=i<=100000 and ch[i][0]==-1:
                Q.append(i)
                ch[i][0]=ch[tmp][0]+1
                ch[i][1]=tmp
            
            


            
            
            
            





