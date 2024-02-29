import sys


def DFS(w,sum,tmp):
    global res   
    if w == 0 :
        if res <sum:
            res = sum
            print(res)
            sys.exit()
        return
    if w <0 :
        if res <sum-tmp:
            res = sum-tmp 
        return
    else:
        for i in range(s):
            ch[i]+=1
            DFS(w-lst[i][0],sum+lst[i][1],lst[i][1])
            ch[i]-=1
        
        
        

if __name__ =="__main__":
    s,w = list(map(int,input().split()))
    lst=[]
    for _ in range(s):
        a,b = map(int,input().split())
        lst.append([a,b,b/a])
    lst.sort(key=lambda x : x[2],reverse=True)
    res=0
    ch = [0]*s
    DFS(w,0,0)
    print(res)

#답안 
#가방의 무게를 기준으로 dy
#냅색 알고리즘

if __name__ =="__main__":
    n,m = list(map(int,input().split()))
    dy=[0]*(m+1)
    for i in range(n):
        w, v = map(int,input().split())
        for j in range(w,m+1):
            dy[j]= max(dy[j],dy[j-w]+v)
            
    print(max(dy))
            
            



    
    
    

    


