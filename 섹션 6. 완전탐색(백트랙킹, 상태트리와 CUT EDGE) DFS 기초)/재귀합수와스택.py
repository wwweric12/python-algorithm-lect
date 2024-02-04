#재귀함수와 스택
import sys
input = sys.stdin.readline

def DFS(x):
    if x>0:
        DFS(x-1) 
        print(x) # stack이여서 1 2 3 으로 출력 


if __name__ == "__main__":
    n= int(input())
    DFS(n)
    