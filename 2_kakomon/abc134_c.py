import sys
input = sys.stdin.readline

n = int(input())
al = []
for i in range(n):
    a = int(input())
    al.append((a,i+1))

al.sort(reverse=True)

for i in range(1,n+1):
    if al[0][1] == i:
        print(al[1][0])
    else:
        print(al[0][0])