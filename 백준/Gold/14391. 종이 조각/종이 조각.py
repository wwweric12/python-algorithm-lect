n, m = map(int,input().split())
lst=[]
for i in range(n):
    tmp=list(input())
    lst.append(tmp)

max_value= 0
ch=[0]*(m*n) # 0,1,2,3,4,5
def DFS(L):
    global max_value
    if L ==n*m:
        #가로
        res=0
       
        for i in range(n):
            tmp=""
            for j in range(m):
                if ch[i*m+j] ==1:
                    tmp+=lst[i][j]
                else:
                    if tmp != "":
                        res+=int(tmp)   
                        tmp=""
            if tmp !="":
                res+=int(tmp)
        
        # 세로 
        for a in range(m):
            tmp=""
            for b in range(n):
                if ch[a+b*m] == 0:   
                    tmp+=lst[b][a]
                else:
                    if tmp !="":
                        res+=int(tmp)
                        tmp=""
            if tmp !="":
                res+=int(tmp)  
        
        if max_value < res:
            max_value=res
                        
        return 
    else:
        ch[L]=1
        DFS(L+1)
        ch[L]=0
        DFS(L+1)
    
            
DFS(0)
print(max_value)