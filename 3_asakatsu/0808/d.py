n,m = map(int, input().split())
fri = [ [False]*(n+1) for _ in range(n+1) ]

for _ in range(m):
    a,b = map(int, input().split())
    fri[a][b] = True
    fri[b][a] = True

ans = []
for i in range(1,n+1):
    val = 0
    for j in range(1,n+1):
        if i == j: continue
        if fri[i][j] == True: continue
        for k in range(1,n+1):
            if i == k: continue
            if fri[i][k] and fri[k][j]:
                val += 1
                break
    ans.append(val)

for a in ans:
    print(a)