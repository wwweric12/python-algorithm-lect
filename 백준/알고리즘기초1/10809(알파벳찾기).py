s = input()
res=[-1]*26


for i in range(len(s)):
    if res[ord(s[i])-97] == -1:
        res[ord(s[i])-97]=i



for i in res:
    print(i,end=' ')