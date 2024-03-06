import sys
from collections import deque


input= sys.stdin.readline
n= int(input())

dQ =deque()


for _ in range(n):
    com =input().split()
    if com[0]=="push":
        dQ.append(com[1])
    elif com[0]== "pop":
        if dQ:
            print(dQ.popleft())
        else:
            print(-1)
    elif com[0] == "size":
        print(len(dQ))
    elif com[0] == "empty":
        if dQ:
            print(0)
        else:
            print(1)
    elif com[0] == "front":
        if dQ:
            print(dQ[0])
        else:
            print(-1)
    elif com[0] == "back":
        if dQ:
            print(dQ[-1])
        else:
            print(-1)
            
            