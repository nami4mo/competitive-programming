def no49(b):
    dp = [ [0]*2 for _ in range(len(b)+1) ]
    dp[0][0] = 1 # same
    dp[0][1] = 0 # small

    for i,bi in enumerate(b):
        bi = int(bi)
        if 0 <= bi <= 3:
            dp[i+1][0] = dp[i][0]
            dp[i+1][1] = dp[i][0]*bi + dp[i][1]*8
        elif bi == 4:
            # dp[i+1][0] = dp[i][0]
            dp[i+1][1] = dp[i][0]*4 + dp[i][1]*8
        elif 5 <= bi <= 8:
            dp[i+1][0] = dp[i][0]
            dp[i+1][1] = dp[i][0]*(bi-1) + dp[i][1]*8
        else:
            # dp[i+1][0] = dp[i][0]
            dp[i+1][1] = dp[i][0]*8 + dp[i][1]*8
    return dp[-1][0] + dp[-1][1]

a,b = map(int, input().split())

b = str(b)
a = str(a-1)

b_no49 = no49(b)
a_no49 = no49(a)
ab_no49 = b_no49 - a_no49
# print(b_no49, a_no49)

all_ab = int(b)-int(a)
ans = all_ab - ab_no49
print(ans)

# for i in range(50):
#     print('---',i)
#     print(no49(str(i)))