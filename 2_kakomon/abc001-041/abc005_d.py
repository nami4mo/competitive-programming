n = int(input())
dl = []
for _ in range(n):
    row = list(map(int, input().split()))
    dl.append(row)


accuml = [ [0]*(n+1) for _ in range(n+1)]
for i in range(n):
    for j in range(n):
        accuml[i+1][j+1] = accuml[i+1][j] + accuml[i][j+1] - accuml[i][j] + dl[i][j]


maxs = [0]*(n**2+1)
for i1 in range(n):
    for j1 in range(n):
        for i2 in range(i1+1,n+1):
            for j2 in range(j1+1,n+1):
                val = accuml[i2][j2] - accuml[i1][j2] - accuml[i2][j1] + accuml[i1][j1]
                area = (i2-i1)*(j2-j1)
                maxs[area] = max(maxs[area], val)

curr_max = 0
for i in range(n**2+1):
    maxs[i] = max(curr_max, maxs[i])
    curr_max = maxs[i]

q = int(input())
ansl = []
for _ in range(q):
    p = int(input())
    ans = maxs[p]
    ansl.append(ans)

for a in ansl:
    print(a)