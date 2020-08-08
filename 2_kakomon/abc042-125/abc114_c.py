ns = input()

dp = [ [ [0]*8  for _ in range(2) ] for _ in range(len(ns)) ]
# dp[i][small_or_not][exist 7,5,3 (0~7)]

first = int(ns[0])
if first > 7:
    dp[0][1][4] = 1
    dp[0][1][2] = 1
    dp[0][1][1] = 1
elif first == 7:
    dp[0][0][4] = 1
    dp[0][1][2] = 1
    dp[0][1][1] = 1
elif first > 5:
    dp[0][1][2] = 1
    dp[0][1][1] = 1
elif first == 5:
    dp[0][0][2] = 1
    dp[0][1][1] = 1
elif first > 3:
    dp[0][1][1] = 1
elif first == 3:
    dp[0][0][1] = 1
dp[0][1][0] = 1

for i in range(0, len(ns)-1):
    next_num = int(ns[i+1])
    dp[i+1][1][0] += dp[i][1][0] 
    for e753 in range(8):
        dp[i+1][1][e753 | 4] += dp[i][1][e753] 
        dp[i+1][1][e753 | 2] += dp[i][1][e753] 
        dp[i+1][1][e753 | 1] += dp[i][1][e753] 

        if next_num > 7:
            dp[i+1][1][e753 | 4] += dp[i][0][e753] 
        if next_num > 5:
            dp[i+1][1][e753 | 2] += dp[i][0][e753] 
        if next_num > 3:
            dp[i+1][1][e753 | 1] += dp[i][0][e753]

        if next_num == 7:
            dp[i+1][0][e753 | 4] += dp[i][0][e753] 
        if next_num == 5:
            dp[i+1][0][e753 | 2] += dp[i][0][e753] 
        if next_num == 3:
            dp[i+1][0][e753 | 1] += dp[i][0][e753]

print( dp[-1][0][7] + dp[-1][1][7])