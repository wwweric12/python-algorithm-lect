import sys 
input = sys.stdin.readline


left_s = list(input().strip())
n = int(input())
right_s = []

for _ in range(n):
    com = list(input().split())
    if com[0] == "P":
        left_s.append(com[1])        
    elif com[0] == "L":
        if left_s:
            tmp=left_s.pop()
            right_s.append(tmp)
    elif com[0] == "D":
        if right_s:
            tmp=right_s.pop()
            left_s.append(tmp)
    elif com[0] == "B":
        if left_s:
            left_s.pop()
    
for _ in range(len(right_s)):
    tmp=right_s.pop()
    left_s.append(tmp)
            
for i in left_s:
    print(i,end='')
    
