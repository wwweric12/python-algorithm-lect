import sys
input =sys.stdin.readline

n= int(input())
lst=list(map(int,input().split()))


ch=[0 for _ in range(n)]
ch_arr=[[] for _ in range(n)]
ch[0]=1
ch_arr[0]=[lst[0]]

for i in range(1,n):
    tmp=0
    for j in range(i-1,-1,-1):
        if lst[j]<lst[i] and ch[j]>tmp:
            tmp=ch[j]
            tmp_arr= [x for x in ch_arr[j]]
            ch_arr[i]=tmp_arr
    ch_arr[i].append(lst[i])
    ch[i]=tmp+1
    
    

print(max(ch))

k=ch.index(max(ch))

for i in ch_arr[k]:
    print(i,end=' ') 
    
        