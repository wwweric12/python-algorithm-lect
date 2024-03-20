t= int(input())


ch=[1]*(12)
ch[2]= 2
ch[3] =4
for i in range(4,12):
    ch[i] = ch[i-1]+ch[i-2]+ch[i-3]
for _ in range(t):
    n= int(input())
    print(ch[n])
    