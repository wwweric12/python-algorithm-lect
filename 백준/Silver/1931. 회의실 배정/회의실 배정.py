n= int(input())
lst=[]
for i in range(n):
    lst.append(list(map(int,input().split())))

lst.sort(key=lambda x : (x[1],x[0]))
cnt=0
end=0
for i in range(n):
    if lst[i][0]>=end:
        cnt+=1
        end=lst[i][1]    

print(cnt)