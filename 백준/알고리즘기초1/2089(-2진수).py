# 내풀이 못품
# import sys

# n= int(input())
# res=''
# cnt=1
# k=abs(n)
# while k>0:
#     k//=2
#     cnt+=1
    

# t=cnt
# ch=[0]*(cnt+2)
# ch[0]=1
# tmp=1


# while cnt+1 !=tmp: 
#     ch[tmp]=(-2)*ch[tmp-1]    
#     if ch[tmp] == n :
#         res+="0"*tmp
#         print(res)
#         sys.exit()
#     tmp+=1
    
# tmp = ch[t]




# while int(tmp)!=n :
#     cnt-=1        
#     if n >tmp and cnt%2==0:
#         tmp+=ch[cnt]
#         res+="1"
#     elif n >tmp and cnt%2 ==1:
#         res+="0"
#     elif n < tmp and cnt%2 ==0:
#         res+="0"
#     elif n<tmp and cnt%2==1:
#         tmp+=ch[cnt]
#         res+="1"


# if len(res) !=t+1:
#     res+="0"*(t+1-len(res))

# print(res)

    
# 답안 
n = int(input())
if n == 0:
    print(0)
else:
    res = ''
    while n != 0:
        remainder = n % (-2)
        n = n // (-2)
        if remainder < 0:
            remainder += 2
            n += 1
        res = str(remainder) + res
    print(res)
  

    