# Bottom-up

n = int(input())
dy=[0]*(n+1)
dy[1]=1 
dy[2]=2 # 2는 1+1, 2 로 2가지 

for i in range(3,n+1):
    dy[i]=dy[i-1] + dy[i-2]
    
print(dy[n])

#top -down

def DFS(len):
    if dy[len]>0: #값이 존재할때는 바로 return 메모리제이션이 되어야 dp가 되는것
        return dy[len]
    if len == 1 or len ==2:  #1이 호출되면 len이 1이니까 1 리턴 2가호출되면 len이 2니깐 1+1,2 로 2를 리턴 
        return len
    else:
        dy[len]=DFS(len-1)+DFS(len-2)
        return dy[len]
    
    
if __name__ =="__main__":
    n= int(input())
    dy=[0]*(n+1)
    print(DFS(n))