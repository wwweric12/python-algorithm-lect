from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    start_point=0
    remain_weight=weight
    Q= deque()
    while start_point!=len(truck_weights):
        answer+=1
        
         # 1초가 지났을때 앞으로 한칸씩 
        for idx in range(len(Q)):
            Q[idx][1] -= 1

        while Q and Q[0][1] == 0:
            weight, _ = Q.popleft()
            remain_weight += weight
        
        
        # 다리에 트럭이 올라갈 수 있을때 
        if start_point!=len(truck_weights) and remain_weight >=truck_weights[start_point]:
            Q.append([truck_weights[start_point],bridge_length])
            remain_weight-=truck_weights[start_point]
            start_point+=1
            
    if Q:
        w, remain=Q.pop()
        answer+=remain
            
    return answer