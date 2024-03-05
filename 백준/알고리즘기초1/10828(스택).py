import sys

input=sys.stdin.readline

n = int(input())

stack=[]

for _ in range(n):
    com = input().split()
    if com[0] == "push":
        stack.append(int(com[1]))
    elif com[0] == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif com[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif com[0]=="size":
        print(len(stack))
    elif com[0] == "empty":
        if stack:
            print(0)
        else:
            print(1)
            
        