n = int(input())

lst=[]
max_length=0
for _ in range(n):
    tmp= input()
    k=len(tmp)    
    lst.append([tmp,k])
    max_length=max(max_length,k)


alphabet={}
res=0

for alpha, length in lst:
    for j in range(length):
        tmp = alpha[j]
        if tmp in alphabet:
            alphabet[tmp] += 10**(length-j-1)
        else:
            alphabet[tmp] = 10**(length-j-1)
        
sorted_alphabet = sorted(alphabet.items(), key=lambda x: x[1], reverse=True)


number=9
for alpha, weight in sorted_alphabet:
    tmp=''
    length =len(str(weight))
    for j in str(weight):
        if j != 0:
            tmp+=str(number*int(j)*10**(length-1))
        else:
            tmp+=j*10**(length-1)
        length-=1
        res+=int(tmp)
        tmp=''
    number-=1

print(res)
        
    



    
        