from copy import copy

w = int(input())
n,k = map(int, input().split())

# dp = [ [ [0]*(w+1)  for _ in range(k+1) ] for _ in range(n+1) ]
dp = [ [0]*(w+1)  for _ in range(k+1) ]
for _ in range(n):
    new_dp = [ [0]*(w+1)  for _ in range(k+1) ]
    a,b = map(int, input().split())
    for ki in range(k+1):
        for wi in range(w+1):
            new_dp[ki][wi] = max(new_dp[ki][wi], dp[ki][wi])
            if a+wi <= w and ki+1 <= k:
                new_dp[ki+1][wi+a] = max(new_dp[ki+1][a+wi], dp[ki][wi]+b)
    dp = copy(new_dp)

ans = 0
for ki in range(k+1):
    for wi in range(w+1):
        ans = max(dp[ki][wi], ans)

print(ans)
