s = input()
res=[""]*len(s)
for i in range(len(s)):
    res[i] = s[i::]
res.sort()

for i in res:
    print(i)