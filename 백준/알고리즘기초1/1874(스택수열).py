import sys 

n = int(input())
stack =[]
res=[]
tmp =0

for _ in range(n):
    k = int(input())
    while k>tmp:
        tmp+=1
        stack.append(tmp)
        res.append("+")
    if stack[-1] == k:
        stack.pop()
        res.append("-")
    else:
        print("NO")
        sys.exit()

for i in res:
    print(i)

