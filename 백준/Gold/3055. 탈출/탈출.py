import sys
from collections import deque

r ,c =map(int,input().split())
lst=[]

dochi=[0,0]
beaver=[0,0]

dx=[-1,0,0,1]
dy=[0,1,-1,0]
ch=[[0 for _ in range(c)] for _ in range(r)]
water_cnt=0
dochi_cnt=1

Q=deque()
water=deque()
for i in range(r):
    tmp = list(input())
    for j in range(c):
        if tmp[j]=="S":
            dochi=[i,j,0]
        elif tmp[j]=="*":
            water.append([i,j])
            water_cnt+=1
        elif tmp[j]=="D":
            beaver=[i,j]
    lst.append(tmp)
            
            

Q.append(dochi)



while Q:
    water_ncnt=0
    for i in range(water_cnt):
        water_x,water_y = water.popleft()
        for i in range(4):
            water_xx = water_x+dx[i]
            water_yy = water_y+dy[i]
            if 0<=water_xx <r and 0<= water_yy<c  and lst[water_xx][water_yy]==".":
                lst[water_xx][water_yy]="*"
                water.append((water_xx,water_yy))
                water_ncnt+=1 
    water_cnt=water_ncnt
    dochi_ncnt=0
    for _ in range(dochi_cnt):
        x,y,cnt=Q.popleft()
        if x==beaver[0] and y == beaver[1]:
            print(cnt)
            sys.exit()
        else: 
            for i in range(4):
                xx= x+dx[i]
                yy= y+dy[i]
                if 0<= xx<r and 0<= yy <c and lst[xx][yy]!="*" and lst[xx][yy]!="X"  and ch[xx][yy]==0:                
                    dochi_ncnt+=1
                    ch[xx][yy]=1
                    Q.append((xx,yy,cnt+1))
    dochi_cnt=dochi_ncnt
        
        
print("KAKTUS")


            
            

        