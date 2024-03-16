n, b =map(int,input().split())

res=''
while n!=0:
    tmp=n%b
    n//=b
    if tmp>9:
        tmp+=55
        tmp=chr(tmp)
    res=str(tmp)+res
print(res)