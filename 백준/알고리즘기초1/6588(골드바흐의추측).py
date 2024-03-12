import sys
input =sys.stdin.readline



ch = [0]*(1000001)
ch[1]=1
for i in range(2,int(1000001**0.5)+1):
    if ch[i]==0:
        for j in range(i*2,1000001,i):
            ch[j]=1
        
while True:
    k=int(input())
    if k ==0:
        break
    else:
        for i in range(3,k+1,2):
            if ch[i]==0 and ch[k-i]==0:
                print(str(k)+" = "+str(i)+" + "+str(k-i))
                break
            
                        
                