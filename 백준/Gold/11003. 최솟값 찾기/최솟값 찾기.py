## 최솟값을 하나 들고 있다가 빠져 나가면 다시 계산?
## 계속해서 갱신이 되는 구조면? 시간초과가 날 것임 
## 그렇다면 어떻게 해야할까?
## 2개 씩 들고 있어야하나? 어차피 하나가 빠지면 그러면 하나를 채워줘야하는데 
## 의미가 없음
## 그러면 어떤식으로든 값들을 들고 있어야하는데 
## 값을 들고있으면서 추가를 할 때 별로 복잡도가 안높은걸 들고 
## 최솟값이 무엇인지 금방 찾을 수 있는 방법이 뭐가 있을까 
## deque를 사용해서 추가와 삭제를 O(1)로 가져가도
## 최솟값을 읽기 위해서는 O(N)이 드는데 

from collections import deque
import sys
input = sys.stdin.readline


n, l = map(int,input().split())
lst = list(map(int,input().split()))





dq= deque()
res=[]



for i in range(n):
    curr = lst[i]

    
    while dq and dq[-1][1] > curr:
        dq.pop()

    dq.append([i,curr])

    if dq[0][0]<=i-l:
        dq.popleft()
    

    res.append(dq[0][1])


for i in res:
    print(i,end=" ")







