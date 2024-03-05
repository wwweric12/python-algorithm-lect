import sys
input = sys.stdin.readline
n = int(input())

for _ in range(n):
    tmp = input().split()
    for i in tmp:
        print(i[::-1],end=' ')
    print()
        