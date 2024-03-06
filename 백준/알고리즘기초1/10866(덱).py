import sys


input = sys.stdin.readline
n= int(input())

first_lst=[]
second_lst=[]

for _ in range(n):
    com =input().split()
    if com[0] == "push_front":
        first_lst.append(com[1])
    elif com[0] == "push_back":
        second_lst.append(com[1])
    elif com[0] == "pop_front":
        if first_lst:
            print(first_lst.pop())
        elif second_lst:
            print(second_lst.pop(0))
        else:
            print(-1)
    elif com[0] == "pop_back":
        if second_lst:
            print(second_lst.pop())
        elif first_lst:
            print(first_lst.pop(0))
        else:
            print(-1)
    elif com[0] == "size":
        print(len(first_lst)+len(second_lst))
    elif com[0] == "empty":
        if not (first_lst or second_lst):
            print(1)
        else:
            print(0)        
    elif com[0] == "front":
        if first_lst:
            print(first_lst[-1])
        elif second_lst:
            print(second_lst[0])
        else:
            print(-1)
        
    elif com[0] == "back":
        if second_lst:
            print(second_lst[-1])
        elif first_lst:
            print(first_lst[0])
        else:
            print(-1)
    
         
    