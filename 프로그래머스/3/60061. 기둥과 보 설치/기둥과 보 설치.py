 
def checkBo(n,x,y,ch_bo,ch_bar):
    if y<=0:
        return False
    if ch_bar[x][y-1]==1:
        ch_bo[x][y]=1
        return True
    elif x+1 <=n and ch_bar[x+1][y-1]==1:
        ch_bo[x][y]=1
        return True
    elif x+1 <=n and x>0 and ch_bo[x-1][y]==1 and ch_bo[x+1][y]==1:
        ch_bo[x][y]=1
        return True
    
    return False
    
    
## 기둥은 바닥이거나(y==0) ,보의 끝부분 위에 있거나, 기둥위거나 
def checkBar(n,x,y,ch_bo,ch_bar):
    if y==0 or ch_bo[x][y]==1 :
        ch_bar[x][y]=1
        return True
    elif x>=1 and ch_bo[x-1][y]==1 :
        ch_bar[x][y]=1
        return True
    elif y>=1 and  ch_bar[x][y-1]==1:
        ch_bar[x][y]=1
        return True
    else:
        return False
        
def checkDel(n,ch_bo,ch_bar):
    for x in range(n):
        for y in range(n):
            if ch_bo[x][y] ==1:
                if checkBo(n,x,y,ch_bo,ch_bar) == False:
                    return False
            if ch_bar[x][y]==1:
                if checkBar(n,x,y,ch_bo,ch_bar) == False:
                    return False 
    return True

def solution(n, build_frame):
    answer = []
    ch_bo=[[0 for _ in range(n+1)] for _ in range(n+1)] 
    ch_bar=[[0 for _ in range(n+1)] for _ in range(n+1)] 
    for build in build_frame:
        x, y, a, b = build
        if a== 0:
            if b==1:
                checkBar(n,x,y,ch_bo,ch_bar)
            else :
                ch_bar[x][y]=0
                if checkDel(n,ch_bo,ch_bar)== False:
                    ch_bar[x][y]=1
                
        else:
            if b== 1:
                checkBo(n,x,y,ch_bo,ch_bar)
            else:
                ch_bo[x][y]=0
                if checkDel(n,ch_bo,ch_bar) == False:
                    ch_bo[x][y]=1
    
    for i in range(n+1):
        for j in range(n+1):
            if ch_bar[i][j]==1:
                answer.append([i,j,0])
            if ch_bo[i][j]==1:
                answer.append([i,j,1])
            
        
    
    return answer





