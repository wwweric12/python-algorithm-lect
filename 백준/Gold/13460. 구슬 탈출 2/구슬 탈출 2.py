n , m = map(int,input().split())

map_list=[]
red=[0,0]
blue=[0,0]
whole=[0,0]

value =100
for i in range(n):
    tmp=list(input())
    for j in range(m):
        if tmp[j]=="R":
            red=[i,j]
        elif tmp[j]=="B":
            blue=[i,j] 
        elif tmp[j]=="O":
            whole=[i,j]
    map_list.append(tmp)



def left(x,y,color):
    prev_x=x
    prev_y=y
    while True:
        x-=1
        if map_list[y][x]=="O":
            map_list[prev_y][prev_x]="."
            return x,y,True
        elif map_list[y][x]=="#" or map_list[y][x]=="R" or map_list[y][x]=="B":
            if prev_x+1 ==x:
                return
            else:
                map_list[prev_y][prev_x]="."
                if color=="red":
                    map_list[y][x+1]="R"
                else:
                    map_list[y][x+1]="B"
            return x+1,y,False
       

def right(x,y,color):
    prev_x=x
    prev_y=y
    while True:
        x+=1
        if map_list[y][x]=="O":
            map_list[prev_y][prev_x]="."
            return x,y,True
        elif map_list[y][x]=="#" or map_list[y][x]=="R" or map_list[y][x]=="B":
            if prev_x-1 ==x:
                return
            else:
                map_list[prev_y][prev_x]="."
                if color=="red":
                    map_list[y][x-1]="R"
                else:
                    map_list[y][x-1]="B"
            return x-1,y,False
        
def up(x,y,color):
    prev_x=x
    prev_y=y
    while True:
        y+=1
        if map_list[y][x]=="O":
            map_list[prev_y][prev_x]="."
            return x,y,True
        elif map_list[y][x]=="#" or map_list[y][x]=="R" or map_list[y][x]=="B":
            if prev_y-1 ==y:
                return
            else:
                map_list[prev_y][prev_x]="."
                if color=="red":
                    map_list[y-1][x]="R"
                else:
                    map_list[y-1][x]="B"
            return x,y-1,False
        
def down(x,y,color):
    prev_x=x
    prev_y=y
    while True:
        y-=1
        if map_list[y][x]=="O":
            map_list[prev_y][prev_x]="."
            return x,y,True
        elif map_list[y][x]=="#" or map_list[y][x]=="R" or map_list[y][x]=="B":
            if prev_y+1 ==y:
                return
            else:
                map_list[prev_y][prev_x]="."
                if color=="red":
                    map_list[y+1][x]="R"
                else:
                    map_list[y+1][x]="B"
            return x,y+1,False
        
def back(red_nx,red_ny,red_x,red_y,blue_nx,blue_ny,blue_x,blue_y,red_state,blue_state):
    if red_state and blue_state:
        map_list[red_ny][red_nx]="O"
        map_list[red_y][red_x]="R"
        map_list[blue_y][blue_x]="B"
    elif red_state and not blue_state:
        map_list[red_ny][red_nx]="O"
        map_list[red_y][red_x]="R"
        map_list[blue_y][blue_x]="B"
        map_list[blue_ny][blue_nx]="."
    elif not red_state and blue_state:
        map_list[red_ny][red_nx]="."
        map_list[red_y][red_x]="R"
        map_list[blue_y][blue_x]="B"
        map_list[blue_ny][blue_nx]="O"
    else:     
        map_list[red_ny][red_nx]="."
        map_list[red_y][red_x]="R"
        map_list[blue_ny][blue_nx]="."
        map_list[blue_y][blue_x]="B"
            

def DFS(L,red_x,red_y,blue_x,blue_y,red_state,blue_state):
    global value
    if L == 11:
        return
    elif red_state and not blue_state:
        value=min(value,L)
        return
    elif blue_state:
        return
    else:
        if red_x<= blue_x and red_y <= blue_y:
            red_nx, red_ny, red_state=left(red_x,red_y,"red")
            blue_nx, blue_ny, blue_state=left(blue_x,blue_y,"blue")
            DFS(L+1,red_nx, red_ny,blue_nx, blue_ny,red_state,blue_state)
            back(red_nx,red_ny,red_x,red_y,blue_nx,blue_ny,blue_x,blue_y,red_state,blue_state)
            blue_nx, blue_ny, blue_state=right(blue_x,blue_y,"blue")
            red_nx, red_ny, red_state=right(red_x,red_y,"red")
            DFS(L+1,red_nx, red_ny,blue_nx, blue_ny,red_state,blue_state)
            back(red_nx,red_ny,red_x,red_y,blue_nx,blue_ny,blue_x,blue_y,red_state,blue_state)
            blue_nx, blue_ny, blue_state=up(blue_x,blue_y,"blue")
            red_nx, red_ny, red_state=up(red_x,red_y,"red")
            DFS(L+1,red_nx, red_ny,blue_nx, blue_ny,red_state,blue_state)
            back(red_nx,red_ny,red_x,red_y,blue_nx,blue_ny,blue_x,blue_y,red_state,blue_state)
            red_nx, red_ny, red_state=down(red_x,red_y,"red")
            blue_nx, blue_ny, blue_state=down(blue_x,blue_y,"blue")
            DFS(L+1,red_nx, red_ny,blue_nx, blue_ny,red_state,blue_state)
            back(red_nx,red_ny,red_x,red_y,blue_nx,blue_ny,blue_x,blue_y,red_state,blue_state)
            
        elif red_x<= blue_x and red_y >= blue_y:
            red_nx, red_ny, red_state=left(red_x,red_y,"red")
            blue_nx, blue_ny, blue_state=left(blue_x,blue_y,"blue")
            DFS(L+1,red_nx, red_ny,blue_nx, blue_ny,red_state,blue_state)
            back(red_nx,red_ny,red_x,red_y,blue_nx,blue_ny,blue_x,blue_y,red_state,blue_state)
            blue_nx, blue_ny, blue_state=right(blue_x,blue_y,"blue")
            red_nx, red_ny, red_state=right(red_x,red_y,"red")
            DFS(L+1,red_nx, red_ny,blue_nx, blue_ny,red_state,blue_state)
            back(red_nx,red_ny,red_x,red_y,blue_nx,blue_ny,blue_x,blue_y,red_state,blue_state)
            red_nx, red_ny, red_state=up(red_x,red_y,"red")
            blue_nx, blue_ny, blue_state=up(blue_x,blue_y,"blue")
            DFS(L+1,red_nx, red_ny,blue_nx, blue_ny,red_state,blue_state)
            back(red_nx,red_ny,red_x,red_y,blue_nx,blue_ny,blue_x,blue_y,red_state,blue_state)
            blue_nx, blue_ny, blue_state=down(blue_x,blue_y,"blue")
            red_nx, red_ny, red_state=down(red_x,red_y,"red")
            DFS(L+1,red_nx, red_ny,blue_nx, blue_ny,red_state,blue_state)
            back(red_nx,red_ny,red_x,red_y,blue_nx,blue_ny,blue_x,blue_y,red_state,blue_state)
            
        elif red_x>= blue_x and red_y <= blue_y:
            blue_nx, blue_ny, blue_state=left(blue_x,blue_y,"blue")
            red_nx, red_ny, red_state=left(red_x,red_y,"red")
            DFS(L+1,red_nx, red_ny,blue_nx, blue_ny,red_state,blue_state)
            back(red_nx,red_ny,red_x,red_y,blue_nx,blue_ny,blue_x,blue_y,red_state,blue_state)
            red_nx, red_ny, red_state=right(red_x,red_y,"red")
            blue_nx, blue_ny, blue_state=right(blue_x,blue_y,"blue")
            DFS(L+1,red_nx, red_ny,blue_nx, blue_ny,red_state,blue_state)
            back(red_nx,red_ny,red_x,red_y,blue_nx,blue_ny,blue_x,blue_y,red_state,blue_state)
            blue_nx, blue_ny, blue_state=up(blue_x,blue_y,"blue")
            red_nx, red_ny, red_state=up(red_x,red_y,"red")
            DFS(L+1,red_nx, red_ny,blue_nx, blue_ny,red_state,blue_state)
            back(red_nx,red_ny,red_x,red_y,blue_nx,blue_ny,blue_x,blue_y,red_state,blue_state)
            red_nx, red_ny, red_state=down(red_x,red_y,"red")
            blue_nx, blue_ny, blue_state=down(blue_x,blue_y,"blue")
            DFS(L+1,red_nx, red_ny,blue_nx, blue_ny,red_state,blue_state)
            back(red_nx,red_ny,red_x,red_y,blue_nx,blue_ny,blue_x,blue_y,red_state,blue_state)
            
        elif red_x>= blue_x and red_y >= blue_y:
            blue_nx, blue_ny, blue_state=left(blue_x,blue_y,"blue")
            red_nx, red_ny, red_state=left(red_x,red_y,"red")
            DFS(L+1,red_nx, red_ny,blue_nx, blue_ny,red_state,blue_state)
            back(red_nx,red_ny,red_x,red_y,blue_nx,blue_ny,blue_x,blue_y,red_state,blue_state)
            red_nx, red_ny, red_state=right(red_x,red_y,"red")
            blue_nx, blue_ny, blue_state=right(blue_x,blue_y,"blue")
            DFS(L+1,red_nx, red_ny,blue_nx, blue_ny,red_state,blue_state)
            back(red_nx,red_ny,red_x,red_y,blue_nx,blue_ny,blue_x,blue_y,red_state,blue_state)
            red_nx, red_ny, red_state=up(red_x,red_y,"red")
            blue_nx, blue_ny, blue_state=up(blue_x,blue_y,"blue")
            DFS(L+1,red_nx, red_ny,blue_nx, blue_ny,red_state,blue_state)
            back(red_nx,red_ny,red_x,red_y,blue_nx,blue_ny,blue_x,blue_y,red_state,blue_state)
            blue_nx, blue_ny, blue_state=down(blue_x,blue_y,"blue")
            red_nx, red_ny, red_state=down(red_x,red_y,"red")
            DFS(L+1,red_nx, red_ny,blue_nx, blue_ny,red_state,blue_state)
            back(red_nx,red_ny,red_x,red_y,blue_nx,blue_ny,blue_x,blue_y,red_state,blue_state)
                
                
DFS(0,red[1],red[0],blue[1],blue[0],False,False)

if value ==100:
    print(-1)
else:
    print(value)
    
    
