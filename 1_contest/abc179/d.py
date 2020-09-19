def dfs():
    pass


def main():
    n,k = map(int, input().split())
    dl = []
    for _ in range(k):
        l,r = map(int, input().split())
        for i in range(l,r+1):
            dl.append(i)

    dl.sort()
    MOD = 998244353
    dp = [0]*(n+1)
    dp[1] = 1
    for i in range(n):
        for d in dl:
            if i+d > n:break
            dp[i+d] += dp[i]
            dp[i+d]%=MOD

    print(dp[n])



if __name__ == "__main__":
    main()