import sys
input = sys.stdin.readline

n = int(input())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))
dp = [[-1]*(n) for _ in range(n)]

lcsums = [0]
rcsums = [0]
for i in range(n):
    v = al[i]*bl[i]
    lcsums.append(lcsums[-1]+v)
    v = al[n-1-i]*bl[n-1-i]
    rcsums.append(rcsums[-1]+v)

ans = 0
for c in range(n):
    v = al[c]*bl[c]
    dp[c][c] = v
    ans = max(ans, v+lcsums[c]+rcsums[n-1-c])
    for d in range(1, n):
        l = c-d
        r = c+d
        if l < 0 or n <= r:
            break
        v = dp[l+1][r-1]+al[r]*bl[l]+al[l]*bl[r]
        dp[l][r] = v
        val = v+lcsums[l]+rcsums[n-1-r]
        if ans < val:
            ans = val

    if c == n-1:
        continue

    v = al[c]*bl[c+1]+al[c+1]*bl[c]
    dp[c][c+1] = v
    ans = max(ans, v+lcsums[c]+rcsums[n-1-c-1])
    for d in range(1, n):
        l = c-d
        r = c+1+d
        if l < 0 or n <= r:
            break
        v = dp[l+1][r-1]+al[r]*bl[l]+al[l]*bl[r]
        dp[l][r] = v
        val = v+lcsums[l]+rcsums[n-1-r]
        if ans < val:
            ans = val

print(ans)
