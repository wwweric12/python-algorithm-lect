n = int(input())
lst = list(map(int,input().split()))

lst.sort()


res = 0

for i in range(n):
    res+=(n-i)*lst[i]
    

print(res)


