n= int(input())

ch= [0]*(n+1)

for i in range(2,n+1):
    ch[i]=ch[i-1]+1
    if i%2 ==0:
        ch[i] = min(ch[i],ch[i//2]+1)
    if i%3 == 0:
        ch[i] = min(ch[i],ch[i//3]+1)
        

print(ch[n])