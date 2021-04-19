r,c,k=map(int, input().split())
dp = [ [ [0]*(c+1)  for _ in range(r+1) ] for _ in range(4) ]

rcv=[[0]*(c+1) for _ in range(r+1)]
for _  in range(k):
    r_,c_,v=map(int, input().split())
    r_-=1
    c_-=1
    rcv[r_][c_]=v

dp[1][0][0]=rcv[0][0]
for i in range(r):
    for j in range(c):
        vr=rcv[i+1][j]
        vc=rcv[i][j+1]
        for cnt in range(4):
            if cnt<3:dp[cnt+1][i][j+1]=max(dp[cnt+1][i][j+1], dp[cnt][i][j]+vc)
            dp[cnt][i][j+1]=max(dp[cnt][i][j+1], dp[cnt][i][j])

            dp[1][i+1][j]=max(dp[1][i+1][j], dp[cnt][i][j]+vr)
            dp[0][i+1][j]=max(dp[0][i+1][j], dp[cnt][i][j])

        # dp[i]

ans=max(dp[0][r-1][c-1],dp[1][r-1][c-1],dp[2][r-1][c-1],dp[3][r-1][c-1])
print(ans)
# print(dp)