import sys
input = sys.stdin.readline

def main():
    r,c,k = map(int, input().split())
    rcv = [ [0]*c for _ in range(r) ]

    for _ in range(k):
        ri,ci,vi = map(int, input().split())
        rcv[ri-1][ci-1] = vi

    # dp[0] = [ [0]*c for _ in range(r) ]
    # dp1 = [ [0]*c for _ in range(r) ]
    # dp2 = [ [0]*c for _ in range(r) ]
    # dp[3] = [ [0]*c for _ in range(r) ]
    dp = [ [ [0]*c  for _ in range(r) ] for _ in range(4) ]


    dp[1][0][0] = rcv[0][0]
    for i in range(r):
        for j in range(c):
            if i+1 < r:
                dp[0][i+1][j] = max(dp[0][i][j], dp[1][i][j], dp[2][i][j], dp[3][i][j], dp[0][i+1][j])
                if rcv[i+1][j] > 0:
                    dp[1][i+1][j] = max(dp[1][i+1][j],  max(dp[0][i][j], dp[1][i][j], dp[2][i][j], dp[3][i][j])+rcv[i+1][j])

            if j+1 < c:
                dp[0][i][j+1] = max(dp[0][i][j], dp[0][i][j+1])
                dp[1][i][j+1] = max(dp[1][i][j], dp[1][i][j+1])
                dp[2][i][j+1] = max(dp[2][i][j], dp[2][i][j+1])
                dp[3][i][j+1] = max(dp[3][i][j], dp[3][i][j+1])
                if rcv[i][j+1] > 0:
                    dp[1][i][j+1] = max(dp[1][i][j+1], dp[0][i][j]+rcv[i][j+1])
                    dp[2][i][j+1] = max(dp[2][i][j+1], dp[1][i][j]+rcv[i][j+1])
                    dp[3][i][j+1] = max(dp[3][i][j+1], dp[2][i][j]+rcv[i][j+1])

    ans = max(dp[0][r-1][c-1], dp[1][r-1][c-1], dp[2][r-1][c-1], dp[3][r-1][c-1])
    print(ans)


if __name__ == "__main__":
    main()