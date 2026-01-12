## 좌표가 10의 9승 이하.. 

import sys 
sys.setrecursionlimit(10**6)
input= sys.stdin.readline

n, q = map(int,input().split())


lst=[]

parents= [i for i in range(n+1)]


def find_parents(node):
    if node == parents[node]:
        return node 
    else:
        parents[node] = find_parents(parents[node])
        return parents[node]
    
def union(a,b):
    parents_a = find_parents(a)
    parents_b = find_parents(b)

    if parents_a <  parents_b:
        parents[parents_b]=parents_a     
    else:
        parents[parents_a] =parents_b



for i in range(n):
    x1, x2 , y = map(int,input().split())
    lst.append((x1,x2,i+1))

lst.sort()


right_max=lst[0][1]
parents_index=lst[0][2]

for i in range(1,n):
    x1,x2,index = lst[i]    
    if right_max>= x1:
        union(index,parents_index)
        if right_max < x2:
            right_max = x2
    else:
        right_max=x2
        parents_index= index


for i in range(q):
    a,b = map(int,input().split())
    if find_parents(a) == find_parents(b):
        print(1)
    else:
        print(0)
        


    


