from collections import deque



def D(num):
    num*=2
    if num>9999:
        num%=10000    
    return num , "D"

def S(num):
    if num==0:
        num=9999
    else:
        num-=1
    return num , "S"

def L(num):
    return (num%1000)*10 +num//1000, "L"

def R(num):
    return (num%10)*1000+num//10  ,"R"


def BFS():
    while Q:
        number,dslr = Q.popleft()
        if ch[number]==1:
            continue
        else:
            ch[number]=1
            if number == end:
                print(dslr)
                break
            for value, alpha in D(number), S(number), L(number), R(number):
                Q.append([value,dslr+alpha])
        
        
T = int(input())
for _ in range(T):
    ch=[0]*10000
    Q=deque()
    start, end = map(int,input().split())
    Q.append([start,""])
    BFS()
    

