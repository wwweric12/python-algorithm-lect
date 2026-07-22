import math

len_nums = 0
nums=''
answer = 0

def solution(numbers):
    global len_nums,nums,answer
    nums=numbers
    
    len_nums = len(numbers)
    visited=[0 for _ in range(len_nums)]
    set_values = set()
    
    def check(num):
        if num <2:
            return False 
        elif num == 2:
            return True
        else:
            for i in range(2,int(math.sqrt(num))+1):
                if num%i == 0:
                    return False 
        
        return True
        
    
    
    def DFS(L,value):
        global nums,len_nums,answer    
        if check(int(value)):
            if int(value) not in set_values:
                set_values.add(int(value))
                answer+=1
                
        for i in range(len_nums):
            if visited[i]==0:
                visited[i] = 1
                DFS(L+1,value+nums[i])
                visited[i] = 0
            
    DFS(0,'0')
            
        
    
    
    return answer