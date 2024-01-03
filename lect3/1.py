

# n= int(input("몇개"))
# for i in range(n):
#     answer=""
#     st = input("문자열입력")
#     st= st.lower()
#     for j in range(len(st)-1,-1,-1):
#         answer+=st[j]
#     if st == answer :
#         # print("#"+str(i+1)+"YES")
#         print("#%d YES" %(i+1))
#     else:        
#         # print("#"+str(i+1)+"NO")
#         print("#%d NO"%(i+1))
        
        

n= int(input("몇개"))

for i in range(n):
    st = input("문자열입력")
    st= st.upper()
    for j in range(len(st)//2):
        if st[j] !=st[-1-j]:
           print("#%d NO"%(i+1))
           break
    else:
        print("#%d YES" %(i+1))


