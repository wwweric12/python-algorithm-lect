n= int(input())


ch=[[0,0] for _ in range(90)]

ch[0]= [0,1]
for i in range(1,90):
    ch[i][0]=ch[i-1][0]+ch[i-1][1]
    ch[i][1]= ch[i-1][0]
    
print(ch[n-1][0]+ch[n-1][1])

