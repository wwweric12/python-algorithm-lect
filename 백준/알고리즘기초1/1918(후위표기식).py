s = input()

stack=[]
res=""
for i in s:
    if i == "(":
      stack.append(i)
    elif i == ")":
        while stack and stack[-1] != "(":
            res+=stack.pop()
        stack.pop()
    elif i == "+" or i == "-":
        while stack and stack[-1] !="(":
            res+=stack.pop()
        stack.append(i) 
    elif i == "*" or i == "/":
        while stack and (stack[-1] == "*" or stack[-1] == "/") and stack[-1] !="(": 
            res+=stack.pop()
        stack.append(i)
    else:
        res+=i

        
        
while stack:
    res+=stack.pop()


print(res)