n= int(input())

ch=[0]*(n+1)

if n>1:
    ch[2]=3


for i in range(4,n+1,2):
    ch[i]= ch[i-2]*ch[2]+2
    for j in range(i-4,-1,-2):
        ch[i]+=ch[j]*2

print(ch[n])