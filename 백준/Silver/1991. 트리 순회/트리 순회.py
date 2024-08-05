n = int(input())

ch=[[] for _ in range(26)]

for _ in range(n):
    center, left,right = input().split()
    ch[ord(center)-65].append(left)
    ch[ord(center)-65].append(right)
    
    

#전위 순회
def PRE_DFS(root):
    if root != ".":
        print(root,end='')
        PRE_DFS(ch[ord(root)-65][0])
        PRE_DFS(ch[ord(root)-65][1])

def CEN_DFS(root):
    if root != ".":
        CEN_DFS(ch[ord(root)-65][0])
        print(root,end='')
        CEN_DFS(ch[ord(root)-65][1])
        
def AFT_DFS(root):
    if root != ".":
        AFT_DFS(ch[ord(root)-65][0])
        AFT_DFS(ch[ord(root)-65][1])
        print(root,end='')

PRE_DFS("A")
print()
CEN_DFS("A")
print()
AFT_DFS("A")
    
    

