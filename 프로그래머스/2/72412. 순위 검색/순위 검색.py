def solution(info, query):
    answer = []
    dict= {}
    for i in info:
        tmp = i.split()
        key = tmp[0]+tmp[1]+tmp[2]+tmp[3]
        if key not in dict:
            dict[key]=[]
        dict[key].append(int(tmp[4]))
    
    

    for key in dict.keys():
        dict[key].sort()
    
    
    for j in query:
        tmp = list(j.replace('and',' ').replace('-',' ').split())
        score=int(tmp.pop())
        keys = list(dict.keys())
        for s in tmp:
            len_keys = len(keys)
            for index in range(len_keys-1,-1,-1):
                if s not in keys[index]:
                    keys.pop(index)
        
        
        res=0
        for key in keys:
            len_key = len(dict[key])
            lt = 0
            rt = len_key
            while lt < rt:
                mid = (lt+rt)//2
                
                if dict[key][mid] >=score:
                    rt=mid
                    
                elif dict[key][mid] <score:
                    lt=mid+1
        
            res+=len_key - lt
            
        answer.append(res)
        
    
    
    
    return answer