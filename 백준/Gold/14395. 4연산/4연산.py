import sys
from collections import deque

s,t = map(int,input().split())

Q= deque()
method=["*","+","-","/"]

ch=set()
Q.append((s,""))
ch.add(s)

if s== t:
    print(0)
    sys.exit()

if t%s ==0 or s%t==0 or t&(t-1)==0:
    while Q:
        num,cal = Q.popleft()
        if num == t:
            print(cal)
            sys.exit()
        else:
            
            for i in range(4):
                if method[i]=="*":
                    n_num=num*num
                elif method[i]=="+":
                    n_num=num+num
                elif method[i]=="-":
                    n_num=0
                elif method[i]=="/" and num!=0:
                    n_num=1
                if 0<=n_num<1000000001 and (n_num not in ch) :
                    ch.add(n_num)
                    Q.append((n_num,cal+method[i]))
                
            
        
print(-1)

    
        