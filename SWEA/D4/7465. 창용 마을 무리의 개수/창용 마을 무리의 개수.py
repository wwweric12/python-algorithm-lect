def find_parents(lst,a):
    if lst[a]!=a:
        lst[a]=find_parents(lst,lst[a])
    return lst[a]

def union_parents(lst,a,b):
    parents_a=find_parents(lst,a)
    parents_b=find_parents(lst,b)
    if parents_a> parents_b:
        lst[parents_a]= parents_b
    else:
        lst[parents_b]= parents_a


t= int(input())
for test_case in range(t):
    n, m = map(int,input().split())
    ch = [i for i in range(n+1)]
    res=1
    for _ in range(m):
        a, b = map(int,input().split())
        union_parents(ch,a,b)
        
    for i in range(1,n+1):
        if i !=ch[i]:
            ch[i]=find_parents(ch,i)
    print("#"+str(test_case+1),end=" ")
    print(len(set(ch))-1)

