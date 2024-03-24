import sys
input = sys.stdin.readline

n = int(input())
ch=[[0,0,0] for _ in range(100001)]
ch[1]=[1,0,0]
ch[2]=[0,1,0]
ch[3]=[1,1,1]
for i in range(4,100001):
    ch[i][0] = (ch[i-1][1]+ch[i-1][2])%1000000009
    ch[i][1]= (ch[i-2][0]+ch[i-2][2])%1000000009
    ch[i][2]= (ch[i-3][0]+ch[i-3][1])%1000000009
    



for _ in range(n):
    k = int(input())
    res=ch[k][0]+ch[k][1]+ch[k][2]
    print(res%1000000009)
    
    