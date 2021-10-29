

def main():
    n=int(input())
    al=list(map(int, input().split()))
    # dp=[[0]*10 for _ in range(10)]
    # dp[al[0]][al[1]]=1
    # for i in range(n):
    #     new_dp=[[0]*10 for _ in range(10)]
    #     a=al[i]
    #     for j in range(10):
    #         for k in range(10):
    #             new_dp[(j+k)]
    dp=[[0]*10 for _ in range(n)]
    dp[0][al[0]]=1
    MOD=998244353
    for i in range(1,n):
        a=al[i]
        for j in range(10):
            dp[i][(j+a)%10]+=dp[i-1][j]
            dp[i][(j*a)%10]+=dp[i-1][j]
            dp[i][(j+a)%10]%=MOD
            dp[i][(j*a)%10]%=MOD
    for i in range(10):
        print(dp[n-1][i])


if __name__ == "__main__":
    main()