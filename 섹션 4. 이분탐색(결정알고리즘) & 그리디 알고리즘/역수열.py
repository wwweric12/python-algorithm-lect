n= int(input())

lst=list(map(int,input().split()))

res=[100]*n
lt=1
tmp=0
cnt=0




while lt<=n:
    if lst[lt-1] == cnt and res[tmp]==100:
        res[tmp]=lt
        lt+=1
        tmp=0
        cnt=0
        continue
    if res[tmp]> lt:
        tmp+=1
        cnt+=1
    else:
        tmp+=1
    
    
        
for i in res:
    print(i,end=' ')



# 답안


# n = int(input())
# a = list(map(int,input().split()))

# seq = [0]*n

# for  i in range(n):
#     for j in range(n):
#         if a[i] == 0 and seq[j] == 0 :
#             seq[j]=i+1
#             break
#         elif seq[j]==0 :
#             a[i]-=1

# for x in seq:
#     print(x, end=' ')