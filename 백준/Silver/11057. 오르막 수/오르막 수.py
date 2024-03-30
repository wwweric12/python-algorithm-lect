n= int(input())

ch=[[1,1,1,1,1,1,1,1,1,1] for _ in range(1001)]

ch[1]=[1,2,3,4,5,6,7,8,9,10]
for i in range(2,1001):
    for j in range(1,10):
        ch[i][j] = (ch[i-1][j]+ch[i][j-1])%10007


print(sum(ch[n-1])%10007)