lst=list(map(str,input()))

stack=[]
cnt=0
for i in range(len(lst)):
    if lst[i] == "(":
        stack.append("(")
    elif lst[i] == ")" and lst[i-1]=="(":
        stack.pop()
        cnt+=len(stack)
    else :
        cnt+=1
        stack.pop()
        
    
print(cnt)


#답안과 동일 

