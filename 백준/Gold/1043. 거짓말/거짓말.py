n, m =map(int,input().split())
kn = set(map(int,input().split()[1:]))

ch=[]
for j in range(m):
    a =set(map(int,input().split()[1:]))
    ch.append(a)
    
for _ in range(m):
    for i in ch:
        if i & kn:
            kn =i| kn
            
cnt =0

for i in ch:
    if not i &kn:
        cnt+=1

print(cnt)