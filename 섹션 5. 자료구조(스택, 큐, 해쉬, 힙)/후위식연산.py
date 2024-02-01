s = input()

stack=[]

for x in s:
    if x.isdecimal():
        stack.append(int(x))
    else:
        tmp1=stack.pop()
        tmp2=stack.pop()
        if x =="+":
            stack.append(tmp2+tmp1)
        elif x=="-":
            stack.append(tmp2-tmp1)
        elif x=="*":
            stack.append(tmp2*tmp1)
        elif x=="/":
            stack.append(tmp2/tmp1)

print(stack[0])

#답안은 풀이와 동일 

