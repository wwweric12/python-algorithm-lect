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


#답안

# s= input()
# stack=[]
# cnt=0
# for i in range(len(s)):
#     if s[i]== "(":
#         stack.append(s[i])
#     else:
#         stack.pop()
#         if s[i-1]=="(":
#             cnt+=len(stack)
#         else:
#             cnt+=1
# print(cnt)