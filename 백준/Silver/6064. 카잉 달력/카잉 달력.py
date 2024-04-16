import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    m,n,x,y =map(int,input().split())
    if m==1:
        print(y)
    elif n==1 :
        print(x)
    
    else :
        cnt=x
        a=x
        b=x
        c=m
        d=m
        b%=n
        if n==y:
            while True:
                if b==0 :
                    print(cnt)
                    break
                if d==0 :
                    print(-1)
                    break
                b+=m
                b%=n
                cnt+=m 
                d+=m
                d%=n 
        
        else:
            while True:
                if b==y :
                    print(cnt)
                    break
                if d==0 :
                    print(-1)
                    break
                b+=m
                b%=n
                cnt+=m 
                d+=m
                d%=n 
                
        
        
