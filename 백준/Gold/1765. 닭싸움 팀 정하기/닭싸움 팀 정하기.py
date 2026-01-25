## 팀의 개수가 최대 


## 친구의 친구는 친구
## 적의 적은 친구
## 사실상 최대의 팀개수가 아니라 

## 나와 친구가 누구인지 + 나와 적이 누구인지를 알아야하는디 
## 나의 적들끼리는 같은 팀이여야함 


import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

friend= [[]for _ in range(n+1)]
enemy = [[]for _ in range(n+1)]

parents= [0 for _ in range(n+1)]


def find_parents(node):
    if parents[node] == 0 or parents[node] == node:
        return parents[node]
    
    parents[node] = find_parents(parents[node])
    return parents[node]



    
def union(a,b):
    parents_a = find_parents(a)
    parents_b = find_parents(b)
    
    if parents_a != 0 and parents_b != 0:
        if parents_b < parents_a:
            parents[parents_a] = parents_b
        else:
            parents[parents_b] = parents_a
    
    elif parents_a == 0 and parents_b == 0:
        if b < a:
            parents[b]= b
            parents[a] = b
        else:
            parents[a] = a
            parents[b] = a
    elif parents_a == 0:
        parents[a] = parents_b
    else:
        parents[b] = parents_a

        
     




for i in range(m):
    r, s, e = input().split()
    s = int(s)
    e = int(e)
    if r == "E":
        enemy[s].append(e)
        enemy[e].append(s)
    else:
        union(s,e)



for i in range(1,n+1):
    if parents[i] == 0:
        parents[i] = i

for i in range(1,n+1):
    if enemy[i] != []:
        min_value= n
        for node in enemy[i]:
            tmp= find_parents(node)
            if tmp != 0:
                min_value= min(min_value,tmp)
        for node in enemy[i]:
            parents[find_parents(node)] =min_value




ch= [0 for _ in range(n+1)]
res=0

for i in range(1,n+1):
    tmp=find_parents(i)
    if ch[tmp] == 0:
        ch[tmp]=1
        res+=1
    


print(res)




