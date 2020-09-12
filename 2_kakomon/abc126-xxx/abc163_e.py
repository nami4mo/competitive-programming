n = int(input())
al = list(map(int, input().split()))

a_val_ind_l = []
for i, a in enumerate(al):
    a_val_ind_l.append((a,i))

a_val_ind_l.sort(reverse=True)
dp = [[0]*(n+1) for _ in range(n+1)]


for i in range(n):
    for j in range(0,n-i):
        dp[i+1][j] = max(dp[i][j] + a_val_ind_l[i+j][0] * abs(a_val_ind_l[i+j][1]-i), dp[i+1][j])
        dp[i][j+1] = max(dp[i][j] + a_val_ind_l[i+j][0] * abs(n-1-a_val_ind_l[i+j][1]-j), dp[i][j+1])


ans = 0
for row in dp:
    row_max = max(row)
    ans = max(row_max, ans)

print(ans)