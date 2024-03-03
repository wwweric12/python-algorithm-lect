n= int(input())

dy=[['']*n for _ in range(n)]

for i in range(n):
    dy[i][i]=0

while True:
    s,d  =map(int,input().split())
    if s== -1 and d == -1:
        break
    else:
        dy[s-1][d-1]=1
        dy[d-1][s-1]=1



for k in range(n): 
    for i in range(n):
        for j in range(n):
            if dy[i][j] == '' and dy[i][k] != ''  and dy[k][j] != '' :
                dy[i][j] = dy[i][k]+dy[k][j]
                dy[j][i] = dy[i][j]
            elif dy[i][j] !='' and dy[i][k] != ''  and dy[k][j] != '' :
               dy[i][j] =min(dy[i][j], dy[i][k]+dy[k][j])
                
    

    
mv = 100
lst =[]

for i in range(len(dy)):
    if mv > max(dy[i]):
        mv = max(dy[i])
        cnt=1
        lst=[i]

    elif mv == max(dy[i]):
        cnt+=1
        lst.append(i)

print(mv,end=' ')
print(cnt)

for i in lst:
    print(i+1,end=' ')
    

#답안

# if __name__ == "__main__":
#     n= int(input())
#     dis=[[100]*(n+1) for _ in range(n+1)]

#     for i in range(1,n+1):
#         dis[i][i]=0

#     while True:
#         s,d  =map(int,input().split())
#         if s== -1 and d == -1:
#             break
#         else:
#             dis[s][d]=1
#             dis[d][s]=1
#     for x in dis:
#         print(x)
#     print()

#     for k in range(1,n+1):
#         for i in range(1,n+1):
#             for j in range(1,n+1):
#                 dis[i][j] = min(dis[i][j],dis[i][k]+dis[k][j])
    
#     for x in dis:
#         print(x)
                
#     res=[0]*(n+1)
#     score = 100
    
#     for i in range(1,n+1):
#         for j in range(1,n+1):
#             res[i]=max(res[i],dis[i][j])
#         score = min(score,res[i])
#     out =[]
#     for i in range(1,n+1):
#         if res[i]==score:
#             out.append(i)
#     print("%d %d" %(score,len(out)))
#     for x in out:
#         print(x,end=' ')            
            
            


            
        
        



