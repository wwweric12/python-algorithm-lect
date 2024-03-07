s = list(input())
stack =[]
que=[]
k =0

while s:
    tmp = s.pop(0)
    if tmp == ">":
        que.append(tmp)
        for i in que :
            print(i,end='')
        que=[]
        k=0
    elif tmp == "<" or k==1:
        for i in stack[::-1]:
            print(i,end='')
        stack=[]
        que.append(tmp)
        k=1
    elif tmp ==" " and k==0:
        for i in stack[::-1]:
            print(i,end='')
        print(" ",end='')
        stack=[]
    elif k==0:
        stack.append(tmp)
    

if stack :
    for i in stack[::-1]:
        print(i,end='')
        
        
    