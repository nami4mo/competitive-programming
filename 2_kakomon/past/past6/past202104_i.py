h,w=map(int, input().split())
al=[list(map(int, input().split())) for _ in range(h)]
dp = [ [ [0]*(h+w+1)  for _ in range(w) ] for _ in range(h) ]
dp[0][0][0]=0
dp[0][0][1]=al[0][0]

for y in range(h):
    for x in range(w):
        for c in range(h+w):
            if y!=0: 
                dp[y][x][c]=max(dp[y-1][x][c], dp[y][x][c])
                dp[y][x][c+1]=max(dp[y-1][x][c]+al[y][x], dp[y][x][c+1])
            if x!=0: 
                dp[y][x][c]=max(dp[y][x-1][c], dp[y][x][c])
                dp[y][x][c+1]=max(dp[y][x-1][c]+al[y][x], dp[y][x][c+1])

for c in range(1,h+w):
    ans=dp[h-1][w-1][c]
    print(ans)