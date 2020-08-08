n,k = map(int, input().split())
al = list(map(int, input().split()))

two_base_1_cnts = [0]*40
for a in al:
    for i in range(40):
        if (a>>i)%2 == 1: two_base_1_cnts[i]+=1

two_base_1_cnts = two_base_1_cnts[::-1]
# print(two_base_1_cnts)

k2 = [0]*40
for i in range(40):
    if (k>>i)%2 == 1: k2[i] = 1
    else: k2[i] = 0

k2 = k2[::-1]
# print(k2)

dp = [ [0]*2 for _ in range(40) ]
# dp[0][0] = 0 # 0 -> small
# dp[0][1] = 0 # 1 -> same

if k2[0] == 1:
    dp[0][0] = (2**39) * two_base_1_cnts[0]
    dp[0][1] = (2**39) * (n-two_base_1_cnts[0])
else:
    dp[0][1] = (2**39) * two_base_1_cnts[0]

for i in range(40-1):
    next_two = 2**(39-i-1)
    if dp[i][0] == 0:
        if k2[i+1] == 1:
            dp[i+1][0] += dp[i][1] + next_two*(two_base_1_cnts[i+1])

    else:
        dp[i+1][0] = max(dp[i][0] + next_two*max(two_base_1_cnts[i+1], n-two_base_1_cnts[i+1]), dp[i][1] + next_two*(two_base_1_cnts[i+1]))
        # dp[i+1][0] = dp[i][0] + next_two*max(two_base_1_cnts[i+1], n-two_base_1_cnts[i+1])
        # dp[i+1][0] += dp[i][1] + next_two*(two_base_1_cnts[i+1])

    if k2[i+1] == 1:
        dp[i+1][1] += dp[i][1] + next_two*(n-two_base_1_cnts[i+1])
    else:
        dp[i+1][1] += dp[i][1] + next_two*(two_base_1_cnts[i+1])
    # print('----',i,'----')
    # print(dp)

print(max(dp[-1][0],dp[-1][1]))