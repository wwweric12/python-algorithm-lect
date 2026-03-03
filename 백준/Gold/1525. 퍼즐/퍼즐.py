
from collections import deque
lst=[]

visited=set()
dy=[-1,0,0,1]
dx=[0,1,-1,0]


zeros=(0,0)

for i in range(3):
    tmp = list(map(int,input().split()))
    for j in range(3):
        if tmp[j] == 0:
            zeros =(i,j)
        lst.append(tmp[j])


Q = deque([])

binary=0

for i in range(9):
    binary |= (lst[i]<<(4*i))


result=[1,2,3,4,5,6,7,8,0]
result_value= 0
for i in range(9):
    result_value |= (result[i]<<(4*i))




Q.append((0,binary,zeros))

res=-1
while Q:
    cnt, binary_value,c_zeros = Q.popleft()
    y,x = c_zeros 
    if binary_value == result_value:
        res= cnt
        break
    if binary_value in visited:
        continue
    visited.add(binary_value)
    for i in range(4):
        xx= x+dx[i]
        yy= y+dy[i]
        tmp_value =binary_value
        if 0<= xx < 3 and 0<= yy <3 :
            tmp = (tmp_value>>(xx+3*yy)*4)&0xF
            tmp_value &=~(0xF <<(xx+3*yy)*4)
            tmp_value |= tmp <<((x+3*y)*4)

            if tmp_value in visited:
                continue
            if tmp_value ==result_value:
                res= cnt+1
                break

            Q.append((cnt+1,tmp_value,(yy,xx)))
    if res != -1:
        break



print(res)




