# n = int(input("N개 자연수 입력 "))
# lst=list(map(int,input(str(n)+"개 자연수 입력").split()))
# t=[]

# def reverse(x):
#     for i in range(len(lst)):
#         tmp= list(str(lst[i]))
#         k=''
#         for j in range(len(tmp)-1,-1,-1):
#             k+=tmp[j]
#         lst[i]=int(k)
#     return x
        
# def isPrime(x):
#     tmp=[]
#     for i in x:
#         if i == 1:
#             tmp.append(i)
#         for j in range(2,i-1):
#             if i%j==0:
#                 tmp.append(i)
#                 break
#     for k in tmp:
#         x.remove(k)
#     print(x)
    
# lst =reverse(lst)

# isPrime(lst)


n = int(input("N개 자연수 입력 "))
lst=list(map(int,input(str(n)+"개 자연수 입력").split()))


def reverse(x):
    res=0
    while x>0 :
        tmp=x%10
        res =res*10+tmp
        x//=10
    return res 

def isPrime(x):
    if x==1:
        return False
    for i in range(2,x//2+1):
        if x%i == 0:
            return False
    else:
        return True
    

for i in lst:
    k = reverse(i)
    if isPrime(k):
        print(k,end=' ')    