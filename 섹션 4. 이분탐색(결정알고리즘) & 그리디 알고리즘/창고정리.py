n = int(input())

lst=list(map(int,input().split()))

t = int(input())

lst.sort()

for _ in range(t):
    lst[n-1]-=1
    lst[0]+=1
    lst.sort()

print(lst[n-1]-lst[0])

#답안과 동일 
    
