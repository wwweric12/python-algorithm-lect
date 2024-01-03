# lst=[]

# for _ in range(7):
#     lst.append(list(map(int,input().split())))

# count =0
# for i in range(7):
#     for j in range(2,5):
#         if lst[i][j-1]==lst[i][j+1] and lst[i][j-2]==lst[i][j+2]:
#             count+=1

# for i in range(2,5):
#     for j in range(7):
#         if lst[i-1][j] == lst[i+1][j] and lst[i-2][j]==lst[i+2][j]:
#             count+=1
            
# print(count)


#답안

board = [list(map(int,input().split())) for _ in range(7)]

cnt =0

for i in range(3):
    for j in range(7):
        tmp=board[j][i:i+5]
        if tmp == tmp[::-1]:
            cnt +=1
        for k in range(2):
            if board[i+k][j] != board[i+5-k-1][j]:
                break
        else:
            cnt+=1
print(cnt)
        