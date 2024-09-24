from collections import deque 

t= int(input())

ch=[0 for _ in range(10001)]

for i in range(2,int(10001**(1/2))+1):
    if ch[i]==1:
        continue
    for j in range(i*i,10001,i):
        ch[j]=1

    

def BFS(start,end):
    Q=deque()
    ch_cnt=[10001 for _ in range(10001)]
    
    Q.append((start,0))
    while Q:
        number, cnt = Q.popleft()
        if int(number) == int(end):
            print(cnt)
            break
        
        number_str = str(number)
        for i in range(4):
            for j in range(10):
                num_lst = list(number_str)
                num_lst[i] = str(j)
                num_str = ''.join(num_lst)
                num = int(num_str)
                
                if ch[num] == 0 and ch_cnt[num] > cnt + 1 and num >= 1000:
                    ch_cnt[num] = cnt + 1
                    Q.append((num, cnt + 1))
                        
            

            
            
            


for k in range(t):
    start,end =input().split()
    BFS(start,end)
    
    

            
        
    
    
