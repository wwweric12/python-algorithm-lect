n= int(input())

lst=[]
ch=[[0,0,0] for _ in range(n+1)]
for _ in range(n):
    tmp = int(input())
    lst.append(tmp)


ch[1][0]= lst[0]
ch[1][1]= lst[0]
ch[1][2]= lst[0]
# 0은 연속x 1은 연속
for i in range(2,n+1):
    # 연속값없음 
    ch[i][0]=ch[i-2][2]+lst[i-1] # 2단계전에 값에+지금값
    ch[i][1]=ch[i-1][0]+lst[i-1] # 이전에 연속 안된값+지금값
    ch[i][2]=max(ch[i][0],ch[i][1])


print(ch[n][2])
    
