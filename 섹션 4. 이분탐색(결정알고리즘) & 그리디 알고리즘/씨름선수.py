# n = int(input())

# lst=[]
# for i in range(n):
#     cm, kg = map(int,input().split())
#     lst.append((cm,kg))

# lst.sort()
# cnt=0

# for i in range(len(lst)):
#     if max(lst,key=lambda x : x[1])==lst[i]:
#         cnt+=1
#     lst[i]=(0,0)
    
# print(cnt)
        

#답안

# n = int(input())

# lst=[]
# for i in range(n):
#     cm, kg = map(int,input().split())
#     lst.append((cm,kg))

# lst.sort(reverse=True)
# largest =0
# cnt =0

# for x, y in lst:
#     if y > largest:
#         largest=y
#         cnt+=1

# print(cnt)


