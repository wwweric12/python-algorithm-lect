n= int(input())


ch = [[1,1] for _ in range(100001)] 


for i in range(1,100001):
    ch[i][0]= (ch[i-1][0] +2*ch[i-1][1] )%9901
    ch[i][1]= (ch[i-1][0] +ch[i-1][1])%9901
    


print(ch[n][0])