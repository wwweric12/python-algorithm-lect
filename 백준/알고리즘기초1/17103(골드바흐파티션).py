import sys
input=sys.stdin.readline

n = int(input())

ch=[0]*1000001
ch[0]=1
ch[1]=1



for i in range(2,int(1000001**0.5)+1):
    if ch[i]==0:
        k=i
        while True:   
           k+=i
           if k>1000000:
               break
           ch[k]=1

 
    
    
    

for i in range(n):
    cnt= 0 
    v = int(input())
    for i in range(2,int(v/2)+1):
        if ch[i] ==0 and ch[v-i]==0:
            cnt+=1
        
    print(cnt)
            


    