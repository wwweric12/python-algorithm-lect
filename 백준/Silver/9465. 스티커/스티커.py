import sys
input = sys.stdin.readline
t= int(input())


for _ in range(t):
    n=int(input())
    lst=[]
    for _ in range(2):
        lst.append(list(map(int,input().split())))
    ch=[[lst[0][0],lst[1][0]] for _ in range(n)]
    if n!=1:
        ch[1]=[lst[1][0]+lst[0][1],lst[0][0]+lst[1][1]]
        for i in range(2,n):
            ch[i][0]=lst[0][i]+max(ch[i-1][1],ch[i-2][0],ch[i-2][1])
            ch[i][1]=lst[1][i]+max(ch[i-1][0],ch[i-2][0],ch[i-2][1])
    
    print(max(ch[n-1][0],ch[n-1][1]))