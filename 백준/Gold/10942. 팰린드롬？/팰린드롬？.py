import sys
input= sys.stdin.readline
n = int(input())
lst=list(map(int,input().split()))
m = int(input())
ch=[[0 for _ in range(n)] for _ in range(n)]


for i in range(n): # 한개일때
    ch[i][i]=1

for i in range(n-1):
    if lst[i] == lst[i+1]: # 2개일때 같으면 1
        ch[i][i+1]=1
    else:                   # 2개일때다르면 0
        ch[i][i+1]=0 
        

for j in range(2,n): # 3개이상 부터 양쪽끝값 같은지 확인 하고 안에가 팰린드롬인지 확인 
    for i in range(n-1):
        if i+j<n:
            if ch[i+1][i+j-1] == 1 and lst[i]==lst[i+j]: # 안에 팰린드롬 + 양쪽같은지 
                ch[i][i+j]=1
            else:
                ch[i][i+j]=0


    
for _ in range(m):
    start,end = map(int,input().split())
    print(ch[start-1][end-1])
    
            
    
            
  
