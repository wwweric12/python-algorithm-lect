import heapq

def solution(k, n, reqs):
    answer = 0
    lst=[]
    ch=[1 for _ in range(k+1)]
    
    def comb(L,start):
        if L == n-k:
            lst.append(ch[:])
        else:
            for i in range(start,k+1):
                ch[i]+=1
                comb(L+1,i)
                ch[i]-=1
                
    comb(0,1)
    
    
    
    def waiting_time(mento):
        nonlocal min_time
        res=0
        for req in reqs:
            start, time, type = req
            while hq[type]:
                end=heapq.heappop(hq[type])    
                if end> start:
                    heapq.heappush(hq[type],end)
                    break
                mento[type]+=1
                    
            if mento[type] !=0:
                heapq.heappush(hq[type],start+time)
                mento[type]-=1
            else:
                end=heapq.heappop(hq[type])
                res+=end-start
                heapq.heappush(hq[type],end+time)
        

        min_time=min(min_time,res)
    
    min_time=100000000
    for tmp_lst in lst:
        hq=[[] for _ in range(k+1)]
        waiting_time(tmp_lst)

    
    return min_time