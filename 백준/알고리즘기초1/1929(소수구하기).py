import sys
input = sys.stdin.readline

m,n = map(int,input().split())
lst=[0]*(n+1)


for i in range(m,n+1):
    if i ==1 :
        lst[i]=1
        continue
    elif i ==2 :
        print(i)
        continue
    elif i %2 == 0:
        lst[i]=1
        continue
    elif lst[i] == 0:
        for j in range(3,int(i**0.5)+1):
            if i%j==0:
                lst[i]=1
                tmp = 2* i
                while tmp <= n:
                    lst[tmp]=1
                    tmp*=2
                break
        else:
            print(i)
            tmp = 2* i
            while tmp <= n:
                lst[tmp]=1
                tmp*=2
                
                        