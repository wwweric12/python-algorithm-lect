n ,k = map(int,input().split())

lst=[]
ch_alpha=[0 for _ in range(26)]
sentence_alpha=[]
for _ in range(n):
    tmp=input()
    tmp_sentence=""
    for alpha in tmp:
        if alpha not in "antic":
            sentence_alpha.append(alpha)
            tmp_sentence+=alpha
    lst.append(tmp_sentence)

sentence_alpha=set(sentence_alpha)

for i in "antic":
    ch_alpha[ord(i)-97]=1
    
sentence_alpha=list(sentence_alpha)
length=len(sentence_alpha)



max_value=0
def DFS_ALPHA(L,start):
    global max_value
    if L ==k:
        value=0
        for sentence in lst:
            for i in sentence:
                if ch_alpha[ord(i)-97]==0:
                    break
            else:
                value+=1
        max_value=max(max_value,value)
    else:
        for i in range(start,length):
            if ch_alpha[ord(sentence_alpha[i])-97]==0:
                ch_alpha[ord(sentence_alpha[i])-97]=1
                DFS_ALPHA(L+1,i)
                ch_alpha[ord(sentence_alpha[i])-97]=0
        



if k <5:
    print(0)
elif k-5>=length:
    print(n)
else:
    DFS_ALPHA(5,0)
    print(max_value)









    