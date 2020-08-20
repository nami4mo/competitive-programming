h,w = map(int, input().split())
al = []
bl = []

for _ in range(h):
    row = list(map(int, input().split()))
    al.append(row)

for _ in range(h):
    row = list(map(int, input().split()))
    bl.append(row)


cl = [ [0]*w for _ in range(h) ]
for i in range(h):
    for j in range(w):
        cl[i][j] = abs(al[i][j] - bl[i][j]) 

INF = 10**9
lim = (h+w)*80//2+1
# dp = [ [INF]*6400 for _ in range(h) ]
dp = [ [ [False]*(lim+1)  for _ in range(w) ] for _ in range(h) ]

dp[0][0][cl[0][0]] = True

for i in range(h):
    for j in range(w):
        for k in range(0,lim+1):
            if dp[i][j][k] == True:
                if i+1 < h:
                    v = cl[i+1][j]
                    if k+v <= lim: dp[i+1][j][k+v] = True
                    dp[i+1][j][abs(k-v)] = True
                if j+1 < w:
                    v = cl[i][j+1]
                    if k+v <= lim: dp[i][j+1][k+v] = True
                    dp[i][j+1][abs(k-v)] = True


for i,v in enumerate(dp[-1][-1]):
    if v == True:
        print(i)
        break