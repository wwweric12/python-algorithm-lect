n= int(input())

ch=[1]*(n+2)
ch[2]=2

for i in range(3,n+1):
    ch[i] = ch[i-1]+ch[i-2]
    
print(ch[n]%10007) 

