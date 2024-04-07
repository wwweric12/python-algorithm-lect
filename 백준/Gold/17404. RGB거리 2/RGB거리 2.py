import sys
input = sys.stdin.readline

n= int(input())
lst=[]
res= 21470000
for _ in range(n):
    lst.append(list(map(int,input().split())))


for i in range(3):
    ch=[[res,res,res] for _ in range(n)]
    ch[0][i]= lst[0][i]
    for j in range(1,n):
        ch[j][0]= min(ch[j-1][1],ch[j-1][2])+lst[j][0]
        ch[j][1]= min(ch[j-1][2],ch[j-1][0])+lst[j][1]
        ch[j][2]= min(ch[j-1][0],ch[j-1][1])+lst[j][2]
    for k in range(3):
        if i !=k:
            res = min(res,ch[-1][k])

print(res)
