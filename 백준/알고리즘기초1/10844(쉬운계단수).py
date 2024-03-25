# n=int(input())


# cnt=0

# def DFS(num,L):
#     global cnt
#     if L==n:
#         cnt+=1
#     else:
#         if str(num)[-1] =="0":
#             DFS(num*10+num+1,L+1)    
#         elif str(num)[-1]=="9":
#             DFS(num*10+num-1,L+1)
#         else:    
#             DFS(num*10+num+1,L+1)
#             DFS(num*10+num-1,L+1)

# if n==1:
#     print(9)
# else:
#     for i in range(1,10):
#         DFS(i,1)
    
# print(cnt%1000000000)


n=int(input())

ch=[[0,1,1,1,1,1,1,1,1,1] for _ in range(101)]

for i in range(1,100):
    ch[i][0]= ch[i-1][1]
    ch[i][9] = ch[i-1][8]
    for j in range(1,9):
        ch[i][j]= ch[i-1][j-1]+ch[i-1][j+1]


print(sum(ch[n-1])%1000000000)


