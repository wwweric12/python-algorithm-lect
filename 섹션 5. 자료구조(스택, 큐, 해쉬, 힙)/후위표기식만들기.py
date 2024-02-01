s=input()

stack=[]
answer=""

sc = {"+":1, "-":1,"*":2,"/":2}
for i in range(len(s)):
    if s[i]== "(" :
        for key in sc:
            sc[key] *= 3
    elif s[i] == ")":
        for key in sc:
            sc[key] /= 3


    if s[i]== "+" or s[i]=="-" or s[i]=="*" or s[i]=="/" :
        while stack and (stack[-1][0] == sc[s[i]] or stack[-1][0] > sc[s[i]]):
            tmp=stack.pop()
            answer+=tmp[1]

    if s[i]== "+" or s[i]=="-" :
        stack.append((sc[s[i]],s[i]))
    elif s[i] =="*" or s[i]=="/":
        stack.append((sc[s[i]],s[i]))
    elif not (s[i] =="(" or s[i] ==")"):
        answer+=s[i]
    


while stack:
    tmp=stack.pop()
    answer+=tmp[1]
    
     
print(answer)

#답안

# a=input()
# stack =[]
# res=''

# for x in a:
#     if x.isdecimal(): #숫자인지 아닌지
#         res+=x
#     else:
#         if x=='(':
#             stack.append(x)
#         elif x=='*' or x=="/":
#             while stack and (stack[-1] == '*' or stack[-1] == '/'): #우선순위가 같을때
#                 res += stack.pop()
#             stack.append(x)
#         elif x=='+' or x=='-':
#             while stack and stack[-1]!='(':
#                 res+= stack.pop()
#             stack.append(x)
#         elif x==')':
#             while stack and stack[-1]!='(':
#                 res+= stack.pop()
#             stack.pop() # "("빼주기

# while stack :
#     res+= stack.pop()

# print(res)
                
            

