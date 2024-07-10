t =int(input())

ch=[1]*10001




for i in range(2,10001):
    ch[i]+= ch[i-2]
    
for i in range(3,10001):
    ch[i]+= ch[i-3]
    
    

for _ in range(t):
    n = int(input())
    print(ch[n]) 
    
    
    