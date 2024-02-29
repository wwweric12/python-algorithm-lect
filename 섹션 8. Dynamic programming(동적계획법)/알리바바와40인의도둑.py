# # bottom -up
# n= int(input())
# lst = [list(map(int,input().split())) for _ in range(n)]
# ch = [[0]*n for _ in range(n)]
# ch[0][0] = lst[0][0]


# for i in range(n):
#     for j in range(n):
#         if i>0 and j>0 :
#             if ch[i-1][j] > ch[i][j-1]:
#                 ch[i][j] = ch[i][j-1] + lst[i][j]
#             else:
#                 ch[i][j] = ch[i-1][j] + lst[i][j]
#         elif i ==0  and j>0:
#             ch[i][j]= ch[i][j-1]+lst[i][j]
#         else: 
#             ch[i][j]= ch[i-1][j]+lst[i][j]            

# print(ch[n-1][n-1])

            
#답안은 풀이와 동일 



#top-down

def DFS(x,y):
    if ch[x][y] !=0:
        return ch[x][y]
    if x== 0  and y==0 :
        return lst[0][0]
    else:
        if y==0:
            ch[x][y]=DFS(x-1,y)+ lst[x][y]
        elif x==0 :
            ch[x][y]= DFS(x,y-1)+ lst[x][y]
        else:
            ch[x][y]= min(DFS(x-1,y),DFS(x,y-1))+lst[x][y]
        return ch[x][y]
    



if __name__ == "__main__":
    n= int(input())
    lst = [list(map(int,input().split())) for _ in range(n)]
    ch = [[0]*n for _ in range(n)]
    print(DFS(n-1,n-1))
    
