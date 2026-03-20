## 전화번호는 길어야 10자리
## t<= 50 , n<=10000

import sys

input = sys.stdin.readline



t = int(input())




for _ in range(t):
    n = int(input())
    flag = 0 
    tree={}
    num_lst =[]
    for i in range(n):
        num = input().strip()
        num_lst.append(num)
    num_lst.sort()
    
    ch = tree
    for num in num_lst:
        tmp = tree
        for k in num:
            if k in tmp:
                flag = 1
            else:
                flag = 0
                tmp[k] ={}
            if "asd" in tmp[k] and flag == 1:
                
                break
            tmp = tmp[k] 
        tmp["asd"] = 0
     
        if flag ==1:
            print("NO")
            break 
    else:
        print("YES")
                
        
    
    
    


