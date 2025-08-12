## 풀이 방법 
## 다이스를 n/2를 가져가서
## 각각의 승/패 비율로 따져서 가장 높은거를 가져가야함 생각해보니 경기수가 정해져 있어서 승 수 로 하면 되겠다.
## 만약 10개 라고 했을 때 5개를 가져가서 따져야하니깐  
## 5개의 경우의 수는 10c5 =252 /2 => 126
## 각각의 번호가 나올 경우의수 6**5*6**5= 6천만..
## 따라서 결국 전부 구해서 하는 방법은 아닌데
## 방법을 찾아야할 듯 


## 생각한 방법
## 1. 합이 높으면 확률이 높다?
## 아니다..
## 2. 생각해보니 주사위를 가져가는 경우의수를 모두 안구하고 반만 구해도 패한 만큼 나머지 반대의 승 이 되는 거기 때문에 반만 하면 되겠다.
## 3. 그래도 시간복잡도가 안될거같은데
## 4. 경우의 수를 다 구하고 가운데 값만 비교해서 더큰 수 가 있는 게 확률이 높다 
## 아니다... 가운데 수가 높다고해서 승률이 높은건 아니다.. .
## 5. 그렇다면 어떻게? 

##구현방법
## 1. 일단 조합으로 각각 주사위를 고를 수 있는 경우의 수 구함 (dfs)
## 2. 그 다음 고른 주사위의 합으로 나올 수 있는 경우의수를 또 구함 
## 3. 배열의 인덱스가 dfs로 구했기 때문에 0번째 인덱스와 끝에 인덱스 가 반대편임
## 4. 그래서 for 문으로 돌면서 A와 B가 어느게 더 많이 이겻는지 비교 
## 5. 비교할 때 미리 배열의합을 sort해서 이중 for문으로 a가 b보다 작은경우 for 문 break하는 방법으로 시간을 아주 조금 줄임
## 6. 한번 비교가 끝나면 max_wins랑 비교해서 어느게 더 큰지 비교 해서 
## 7. 최종적으로 return



def solution(dice):
    answer = []
    cnt_dice=len(dice)
    ch=[0 for _ in range(cnt_dice)]
    cnt=0
    
    lst=[]
    lst_index=[]
    
    tmp=[]
    tmp_index=[]
    
    final_lst=[]
    max_win=0
    max_index=0
    
    
    def DFS(L,start):
        if L == cnt_dice//2:  
            lst.append(tmp[:])
            lst_index.append(tmp_index[:])
            return 
        else:
            for i in range(start,cnt_dice):
                if ch[i]==0:
                    ch[i]=1
                    tmp.append(dice[i])
                    tmp_index.append(i+1)
                    DFS(L+1,i)
                    tmp_index.pop()
                    tmp.pop()
                    ch[i]=0

    DFS(0,0)
    
    def custom_binary_search(lst,target):
        low =0
        high = len(lst)
        while low< high:
            mid =(low+high)//2
            if target >lst[mid]:
                low=mid+1
            else:
                high=mid
        return low
        
        
        
    
    
    def DFS_sum(L,sum_value,length_array):
        if L == length_array:
            sum_lst.append(sum_value)
        else:
            for i in arrays[L]:
                DFS_sum(L+1,sum_value+i,length_array)

    res_cnt=0
    cnt=0
        
    for arrays in lst:
        sum_lst=[]
        DFS_sum(0,0,len(arrays))
        sum_lst.sort()
        final_lst.append(sum_lst)
    

        
    
    for i in range(len(lst)):
        a_win=0
        
        a_lst = final_lst[i]
        b_lst = final_lst[len(final_lst)-1-i]
        
                           
        for a in a_lst:
            win = custom_binary_search(b_lst,a)
            a_win+=win
        
                           
                           
        if max_win >a_win:
            continue
        else:
            max_win =a_win
            max_index= i
        
    
    
    return lst_index[max_index]






