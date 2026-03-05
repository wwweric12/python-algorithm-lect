from collections import deque


while True:
    lst=list(map(int,input().split()))    
    n = lst[0]
    if n == 0 :
        break 
    array = lst[1:]

    Q = deque([(0,0)])

    res= 0 
    tmp_index=0
    for i in range(n):
        tmp_index =i+1
        while Q and Q[-1][1]> array[i]:
            index, value = Q.pop()
            res = max(res,value*((i+1)-index))
            tmp_index= index
        Q.append((tmp_index,array[i]))

    while Q:
        index, value = Q.pop()
        res = max(res,value*((n+1)-index))
    
    print(res)
            

