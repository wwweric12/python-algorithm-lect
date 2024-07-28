from collections import deque
s = int(input())
Q=deque()


view_clip = [1,0,0]
Q.append(view_clip)

ch=[[] for _ in range(1001)]


while True:
    tmp = Q.popleft()
    if tmp[0] == s:
        print(tmp[2])
        break
    elif 0<=tmp[0]<=1000  and  tmp[1] not in ch[tmp[0]]:
        Q.append([tmp[0]-1,tmp[1],tmp[2]+1])
        Q.append([tmp[0],tmp[0],tmp[2]+1])
        Q.append([tmp[0]+tmp[1],tmp[1],tmp[2]+1])
        ch[tmp[0]].append(tmp[1])
    

        
            
        
    
    
