n = int(input())
lst=list(map(int,input().split()))



arr=[lst[0]]

for i in range(1,n):
    if lst[i]>arr[-1]:
        arr.append(lst[i])
    else:
        start=0
        end=len(arr)-1 
        while start <=end:
            mid =(start+end)//2
            if arr[mid] <lst[i]:
                start = mid +1
            else:
                end = mid -1 
        arr[start]=lst[i]

print(len(arr))

