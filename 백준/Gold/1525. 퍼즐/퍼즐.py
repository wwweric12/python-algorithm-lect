
from collections import defaultdict,deque
lst=[]

visited=defaultdict()
dy=[-1,0,0,1]
dx=[0,1,-1,0]


zeros=(0,0)

for i in range(3):
    tmp = list(input().split())
    for j in range(3):
        if tmp[j] == "0":
            zeros =(i,j)
        lst.append(tmp[j])


Q = deque([])

Q.append((0,lst,zeros))

res=-1
while Q:
    cnt, array,c_zeros = Q.popleft()
    y,x = c_zeros
    array_str = "".join(array)
    if array_str == "123456780":
        res= cnt
        break
    if array_str in visited:
        continue
    visited[array_str]=1
    for i in range(4):
        xx= x+dx[i]
        yy= y+dy[i]
        tmp_array = array[:]
        if 0<= xx < 3 and 0<= yy <3 :
            tmp_array[x+y*3], tmp_array[xx+yy*3] = tmp_array[xx+yy*3], tmp_array[x+y*3]
            tmp_array_str = "".join(tmp_array)
            if tmp_array_str in visited:
                continue
            if tmp_array_str =="123456780":
                res= cnt+1
                break

            Q.append((cnt+1,tmp_array,(yy,xx)))
    if res != -1:
        break



print(res)










