n = int(input())
dl = []
for _ in range(n):
    row = list(map(int, input().split()))
    dl.append(row)


accuml = [ [0]*(n+1) for _ in range(n+1)]
for i in range(n):
    for j in range(n):
        accuml[i+1][j+1] = accuml[i+1][j] + accuml[i][j+1] - accuml[i][j] + dl[i][j]


ansl = [0]*(n**2+1) 
for i1 in range(n):
    for j1 in range(n):
        for i2 in range(i1+1,n+1):
            for j2 in range(j1+1,n+1):
                v = accuml[i2][j2] + accuml[i1][j1] - accuml[i2][j1] - accuml[i1][j2]
                s = (i2-i1)*(j2-j1)
                ansl[s] = max(ansl[s],v)

c_max = 0
for i in range(n**2+1):
    c_max = max(ansl[i], c_max)
    ansl[i] = c_max


ans = []    
q = int(input())
for _ in range(q):
    p = int(input())
    ans.append(ansl[p])

for a in ans: print(a)