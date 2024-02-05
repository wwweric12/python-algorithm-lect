# 전역변수 지역변수
def DFS1():
    cnt=3
    print(cnt) #지역변수부터 확인 없으면 전역변수확인
    
    
def DFS2():
    #  global cnt 전역변수로 
    if cnt ==5:
        cnt=cnt+1 # 지역변수로 언어변역이 되서 에러
        print(cnt)
        
        
if __name__ == "__main__":
    cnt=5
    DFS1()
    DFS2()
    print(cnt)
    
################################################
    

def DFS():
    a[0] =7
    print(a)

if __name__ == "__main__":
    a=[1,2,3]
    DFS()
    print(a)