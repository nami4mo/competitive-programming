n,m = map(int, input().split())
cnts = [0]*(n+1)
for _ in range(m):
    a,b = map(int, input().split())
    cnts[a] += 1
    cnts[b] += 1

for c in cnts:
    if c%2 == 1:
        print('NO')
        exit()
else:
    print('YES')