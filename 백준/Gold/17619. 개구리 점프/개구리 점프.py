## 좌표가 10의 9승 이하.. 



n, q = map(int,input().split())


lst=[]

parents= [i for i in range(n+1)]

for i in range(n):
    x1, x2 , y = map(int,input().split())
    lst.append((x1,x2,y,i+1))

lst.sort()

for i in range(1,n):
    px1, px2, py,pindex = lst[i-1]
    x1, x2, y , index = lst[i]

    if y == py:
        continue
    elif x1 <= px2 :
    
        parents[index] = parents[pindex]


for i in range(q):
    a,b = map(int,input().split())
    if parents[a] == parents[b]:
        print(1)
    else:
        print(0)
        


    


