# import sys
# input = sys.stdin.readline

ansl = []
for _ in range(int(input())):
    n = int(input())
    al = list(map(int, input().split()))
    al.append(0)
    INF = 10**5
    dp_me = [INF]*(n+5)
    # dp_fr = [INF]*(n+1)
    dp = [INF]*(n+5)
    dp[0] = 0
    for i in range(n):
        dp[i+2] = min(dp[i]+al[i], dp[i+2])
        dp[i+3] = min(dp[i]+al[i], dp[i+3])
        dp[i+3] = min(dp[i]+al[i]+al[i+1], dp[i+3])
        dp[i+4] = min(dp[i]+al[i]+al[i+1], dp[i+4])

    ans = min(dp[n:n+5])
    ansl.append(ans)

for ans in ansl: print(ans)