## 회전을 할 수 있다. => 회전별로 갖고 있어야하나?
## 어떻게 갖고 있어야할까 => 

## 1: 오른쪽 ,2 : 아래, 3: 왼쪽, 4: 위 
## 1 2 2 2 1
## 2 3 3 3 2
## 회전을 나타내는건 숫자로 왼쪽 위를 기준으로 하면될거같다
## 그리고 +1 씩하면된다
## 그러면 만약에 방향이 양방향이 된다면 
## 1 ,[2,4] # 이건 아닌데 어떻게 나타내지 

from collections import deque 


def rotate(array):
    result = []
    for y, x in array:
        result.append([x, -y])
    
    # 정규화
    min_y = min(y for y, x in result)
    min_x = min(x for y, x in result)

    for i in range(len(result)):
        result[i][0] -= min_y
        result[i][1] -= min_x
    
    return result
    

        



def solution(game_board, table):
    answer = 0
    Q=deque([])
    len_table= len(table)
    
    dy=[-1,0,0,1]
    dx=[0,1,-1,0]
    
    puzzle ={1:[],2:[],3:[],4:[],5:[],6:[]}
    
    
    for x in range(len_table):
        for y in range(len_table):
            if table[y][x] == 1:
                Q.append((y,x))
                tmp=[[y,x]]
                cnt=1
                min_y = y
                min_x = x
                table[y][x]=0
                
                while Q:
                    node_y,node_x =Q.popleft()
                    min_y = min(min_y,node_y)
                    min_x = min(min_x,node_x)
                    for i in range(4):
                        xx= node_x+dx[i]
                        yy= node_y+dy[i]
                        if 0<= xx<len_table and 0<= yy<len_table and table[yy][xx]==1:
                            Q.append((yy,xx))
                            table[yy][xx]=0
                            tmp.append([yy,xx])
                            cnt+=1
                
                for i in range(len(tmp)) :
                    tmp[i][0]-=min_y
                    tmp[i][1]-=min_x
                puzzle[cnt].append(tmp)
                
    ## game_board                 
    for x in range(len_table):
        for y in range(len_table):
            if game_board[y][x] ==0:
                Q.append((y,x))
                tmp=[[y,x]]
                cnt=1
                min_y = y
                min_x = x
                game_board[y][x]=1
                
                while Q:
                    node_y,node_x =Q.popleft()
                    min_y = min(min_y,node_y)
                    min_x = min(min_x,node_x)
                    for i in range(4):
                        xx= node_x+dx[i]
                        yy= node_y+dy[i]
                        if 0<= xx<len_table and 0<= yy<len_table and game_board[yy][xx]==0:
                            Q.append((yy,xx))
                            game_board[yy][xx]=1
                            tmp.append([yy,xx])
                            cnt+=1
                
                for i in range(len(tmp)) :
                    tmp[i][0]-=min_y
                    tmp[i][1]-=min_x
                    
                ## 여기서 cnt안에 있는지 확인인데 
                ## 지금 회전만 처리해주면되는디 
                ## 시계회전 
                ## (x,y) -> (-y,x)
                
                
                flag =0
                for i in range(4):
                    if i!= 0:
                        tmp=rotate(tmp)
                    for puz_index in range(len(puzzle[cnt])) :
                        for node in puzzle[cnt][puz_index]:
                            if node not in tmp:
                                break
                        else:
                            flag=1
                            puzzle[cnt].pop(puz_index)
                            answer+=cnt
                            break
                    if flag == 1:
                        break
                    

    
    
    
    return answer