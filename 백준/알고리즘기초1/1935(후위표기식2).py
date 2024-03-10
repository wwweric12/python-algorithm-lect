n= int(input())
k = input()
stack = []
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
q=dict()
res=0

for i in range(n):
    a=int(input())
    q[alpha[i]] = a      
    

for i in k:
    if i == "*":
        tmp = stack.pop()
        stack[-1]=stack[-1]*tmp
    elif i == "+":
        tmp = stack.pop()
        stack[-1]=stack[-1]+tmp
    elif i == "/":
        tmp = stack.pop()
        stack[-1]=stack[-1]/tmp
    elif i == "-":
        tmp = stack.pop()
        stack[-1]=stack[-1]-tmp
    else:
        stack.append(q[i])


print("{:.2f}".format(stack[-1]))


    