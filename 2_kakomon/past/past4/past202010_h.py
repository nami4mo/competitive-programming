n,m,k = map(int, input().split())
sl = []
for _ in range(n):
    s = list(map(int,input()))
    sl.append(s)

cnts09 = []
for num in range(10):
    csums = [ [0]*(m+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(m):
            v = 1 if sl[i][j] == num else 0
            csums[i+1][j+1] = csums[i+1][j] + csums[i][j+1] - csums[i][j] + v
    cnts09.append(csums)

minnm = min(n,m)
for l in range(minnm,0,-1):
    for ys in range(n):
        for xs in range(m):
            yb = ys+l-1
            xb = xs+l-1
            if yb >= n: continue
            if xb >= m: continue
            max_cnt = 0
            for num in range(10):
                # print(num,yb,xb)
                cnt = cnts09[num][yb+1][xb+1] - cnts09[num][yb+1][xs] - cnts09[num][ys][xb+1] + cnts09[num][ys][xs]
                max_cnt = max(max_cnt,cnt)
            need = l*l-max_cnt
            if need <= k:
                print(l)
                exit()
