MOD = 10**9+7
n,k = map(int, input().split())

half = int(n**0.5)
nums = [-1]*(half*2+1)

nl = half*2+1
# print(nl)

for i in range(1,half+1):
    if i*i > n: break
    if i*i == n:
        pass
    nums[i] = 1
    cnt = max(n//i - max(n//(i+1),half), 0)
    nums[nl-i] = cnt

# print(nums)
dp = [ [0]*(nl) for _ in range(k+1) ]
dp[0][0] = 1
for i in range(k):
    sdp = [0]*(nl+1)
    for j in range(0,nl):
        sdp[j+1] = (sdp[j]+dp[i][j])%MOD
    for j in range(1,nl):
        # dp[i+1][j] = (sdp[nums[j][1]] * nums[j][0])%MOD
        dp[i+1][j] = (sdp[nl-j+1] * nums[j])%MOD
    # print(dp)

ans = sum(dp[k])%MOD
print(ans)