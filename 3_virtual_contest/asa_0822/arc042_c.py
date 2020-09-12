n,p = map(int, input().split())
abl = []
for _ in range(n):
    a,b = map(int, input().split())
    abl.append((a,b))

abl.sort(reverse=True)

# dp = [ [0]*(p+1) for _ in range(n+1) ]
over_max = 0

curr_dp = [0]*(p+1)
for i in range(n):
    next_dp = [0]*(p+1)
    a,b = abl[i]
    for j in range(p+1):
        next_dp[j] = max(curr_dp[j], next_dp[j])
        if j+a <= p:
            next_dp[j+a] = max(next_dp[j+a], curr_dp[j]+b)
        else:
            over_max = max(over_max, curr_dp[j]+b)
    curr_dp = next_dp[:]

ans = max(curr_dp)
ans = max(ans,over_max)
print(ans)