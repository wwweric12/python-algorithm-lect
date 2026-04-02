n = int(input())


# 1->2 
# 2->5
# 3->5
# 4->4
# 5->5
# 6->6
# 7->3
# 8->7
# 9->6 # 무조건 6을 써야함 
# 0->6






for _ in range(n):
    t = int(input())
    ## 가장 큰 경우는 일단 자리수가 많아야하므로 가장 적은 1이 우선으로 쭉 나와야함
    ## 근데 홀수라면? 맨앞을 7로 바꾸면 끝

    cnt =t//2
    max_value=""
    min_value=""
    
    if t%2 ==1:
        max_value = "7"
        max_value+= (cnt-1)*"1"
    
    else:
        max_value+= cnt*"1"


 
    dp=[float('inf') for _ in range(101)]
    dp[2] = 1
    dp[3] = 7
    dp[4] = 4
    dp[5] = 2
    dp[6] = 0
    dp[7] = 8

    lst=[("0",6),("1",2),("2",5),("4",4),("7",3),("8",7)]


    dp_values=[[] for _ in range(101)]
    dp_values[2].append("1")
    dp_values[3].append("7")
    dp_values[4].append("4")
    dp_values[5].append("2")
    dp_values[6].append("0")
    dp_values[7].append("8")

    

    for i in range(8,101):
        leng = (i-1)//7+1 
        for j in range(6):
            value, price =lst[j]
            if i-price<=1:
                continue
            for k in dp_values[i-price]:
                if dp[i] == float('inf'):
                    dp[i] = value+k
                    dp_values[i].append(dp[i])
                else:
                    tmp = value+k
                    if len(tmp) != leng:
                        continue
                    dp_values[i].append(tmp)
                    dp[i] = tmp
                    break



    min_values=[float('inf') for _ in range(101)]

    for i in range(2,101):
        tmp= min_values[i]
        for j in dp_values[i]:
            if j[0] == "0":
                j ="6"+ j[1:]
            tmp=min(tmp,int(j))
        min_values[i] = tmp

    print(min_values[t],end=" ")
    print(max_value)

