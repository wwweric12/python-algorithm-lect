## 자르는데 가장 긴 나무 조각을 가장 짧게 자르기 

## 그러면 일정한 비율로 k 만큼 자르는게 가장 짧게 자를 수 있을 거같다
## 그렇다면 이것을 어떤 기준으로 나눌 수 있을까? 자를 수 있는곳도 정해져 있기 때문에
## 10000개까지 자를 수 있기 때문에 최악의 경우 는 10000C 5000임..
## 심지어 길이도 10억 이고




l, k, c = map(int,input().split())

cut = list(set(map(int,input().split())))
cut.sort()

len_cut= len(cut)
c= min(len_cut,c)


def cut_tree(dist):
    if dist == 0: 
        return float('inf'), -1 
    tmp = l
    cnt = 0
    for i in range(len_cut-1,-1,-1):
        diff = tmp-cut[i]
        if i!=0 and cut[i]-cut[i-1] > dist :
            return float('inf'),-1
        if diff > dist:
            cnt+=1
            if i+1 == len_cut:
                return float('inf'),-1
            tmp = cut[i+1]
    
    
    if cnt > c:
        return float('inf'), -1
    if cnt <c:
        tmp =cut[0]

    if tmp > dist:
        return float('inf'), -1
    
    
    return dist, tmp
        

lt = 0
rt = l

max_dist=0
first_cut=0
while lt <= rt :
    mid = (lt+rt)//2
    dist, first =cut_tree(mid)
    if dist != float('inf'):
        max_dist = dist
        first_cut=first 
        rt=mid-1
    else:
        lt=mid+1


print(max_dist,first_cut)
        


