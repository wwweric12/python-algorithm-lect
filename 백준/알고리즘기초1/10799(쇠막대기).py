s=list(input())

res=0
stack=[]

for i in range(len(s)):
    if s[i] == "(":
        stack.append("(")
    elif s[i]==")" and s[i-1]=="(":
        stack.pop()
        res+=len(stack)
    elif s[i]==")" :
        stack.pop()
        res+=1
    
        
print(res)


