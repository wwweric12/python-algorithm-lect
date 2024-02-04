hq=[]


    

while True:
    n = int(input())
    if n==0:
        if hq:
            tmp=hq.pop(0)
            print(tmp)
            if len(hq)>2:
                h=hq.pop(-1)
                hq.insert(0,h)
                i=0
                while True:
                    left = 2*i+1
                    right = 2*i+2
                    if left > len(hq)-1 or right >len(hq)-1:
                        break
                    elif hq[i]>hq[left] or hq[i] >hq[right]:
                        if hq[left] < hq[right]:
                            if hq[left] < hq[i]:
                                hq[i] ,hq[left] =  hq[left],hq[i]
                                i= left
                            else:
                                break
                        else: 
                            if hq[right] < hq[i]:
                                hq[i] ,hq[right] =  hq[right],hq[i]
                                i= right
                            else:
                                break
                    else:
                        break
            else:
                 hq.sort()   
                        
                    
        else:
            print(-1)
    elif n==-1:
        break
    else:
        hq.append(n)
        ln = len(hq)-1
        while ln>0:
            if hq[(ln-1)//2] > hq[ln]:
                hq[(ln-1)//2] , hq[ln] = hq[ln] ,hq[(ln-1)//2] 
                ln=(ln-1)//2
            else:
                break
       
            
        


        

# 최소힙은 부모노드가 자식노드 보다 작아야함
# 루트노드가 pop되면 마지막값이 루트노드로 오게됨
# 두자식 값중에 작은값이랑 비교

#답안 

# import heapq as hq

# a=[]
# while True:
#     n= int(input())
#     if n == -1:
#         break
#     if n == 0:
#         if len(a) == 0:
#             print(-1)
#         else:
#             print(hq.heappop(a)) # a에서 루트노드값을 pop시켜서 return
#     else:
#         hq.heappush(a,n) # a라는 list에  최소 heap의형태로 n값을 넣어줌