

n= int(input())

for _ in range(n):
    tmp =input()
    res=[]
    for i in tmp:
        if i == "(":
            res.append("(")
        elif i ==")":
            if res and res[-1]== "(":
                res.pop()
            else:
                res.append(")")
    
    for j in res:
        if j =="(" or j==")":
            print("NO")
            break
    else:
        print("YES")   
        
                
            
            
    
    