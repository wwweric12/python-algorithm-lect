n, k = map(int,input().split())

ch=[[0]*(202) for _ in range(202)]


for i in range(1,202):
    ch[i][1] = 1
    ch[i][2] = i+1
    ch[1][i]= i 

for i in range(2,202):
    for j in range(2,202):
        ch[i][j]=(ch[i][j-1]+ch[i-1][j])% 1000000000
        
print(ch[n][k])



